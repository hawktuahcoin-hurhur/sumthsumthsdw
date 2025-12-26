"""
AI-powered features for novel reading: summarization, embeddings, character tracking, etc.
"""
import json
import warnings
import numpy as np
from typing import List, Dict
import textstat

# Suppress transformer warnings
warnings.filterwarnings('ignore')

try:
    from sentence_transformers import SentenceTransformer
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    EMBEDDINGS_AVAILABLE = False

try:
    from transformers import pipeline
    SUMMARIZER_AVAILABLE = True
except ImportError:
    SUMMARIZER_AVAILABLE = False

try:
    import spacy
    NLP_AVAILABLE = True
except ImportError:
    NLP_AVAILABLE = False


class AIFeatures:
    """Manages AI features for novel reading."""
    
    def __init__(self):
        """Initialize AI models."""
        self.embeddings_model = None
        self.summarizer = None
        self.nlp_model = None
        self._load_models()
    
    def _load_models(self):
        """Load AI models (lazy loaded)."""
        pass  # Models will be loaded on first use
    
    def _ensure_embeddings_model(self):
        """Lazy load embeddings model."""
        if EMBEDDINGS_AVAILABLE and self.embeddings_model is None:
            try:
                self.embeddings_model = SentenceTransformer('all-MiniLM-L6-v2')
            except Exception as e:
                print(f"Failed to load embeddings model: {e}")
    
    def _ensure_summarizer(self):
        """Lazy load summarizer model."""
        if SUMMARIZER_AVAILABLE and self.summarizer is None:
            try:
                self.summarizer = pipeline('summarization', 
                                          model='facebook/bart-large-cnn',
                                          device=-1)  # CPU
            except Exception as e:
                print(f"Failed to load summarizer model: {e}")
    
    def _ensure_nlp_model(self):
        """Lazy load spaCy NLP model."""
        if NLP_AVAILABLE and self.nlp_model is None:
            try:
                self.nlp_model = spacy.load('en_core_web_sm')
            except OSError:
                print("Downloading spaCy model...")
                import subprocess
                subprocess.run(['python', '-m', 'spacy', 'download', 'en_core_web_sm'])
                self.nlp_model = spacy.load('en_core_web_sm')
            except Exception as e:
                print(f"Failed to load NLP model: {e}")
    
    def generate_summary(self, text: str, max_length: int = 150, min_length: int = 50) -> str:
        """
        Generate abstractive summary of text using BART.
        
        Args:
            text: Text to summarize
            max_length: Maximum summary length
            min_length: Minimum summary length
            
        Returns:
            Summary text or original text if summarization fails
        """
        if not SUMMARIZER_AVAILABLE:
            return self._extractive_summary(text, max_length)
        
        try:
            self._ensure_summarizer()
            
            # Split into sentences and take first 1024 tokens
            sentences = text.split('.')
            text_to_summarize = '. '.join(sentences[:10])  # Limit to first ~10 sentences
            
            if len(text_to_summarize.split()) < min_length:
                return text[:300] + "..."  # Too short to summarize
            
            summary = self.summarizer(text_to_summarize, 
                                     max_length=max_length, 
                                     min_length=min_length,
                                     do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Summarization error: {e}")
            return self._extractive_summary(text, max_length)
    
    def _extractive_summary(self, text: str, max_words: int = 50) -> str:
        """Fallback: create simple extractive summary."""
        words = text.split()[:max_words]
        return ' '.join(words) + "..."
    
    def generate_embeddings(self, text: str) -> List[float]:
        """
        Generate embedding vector for text.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector as list of floats
        """
        if not EMBEDDINGS_AVAILABLE:
            return []
        
        try:
            self._ensure_embeddings_model()
            embedding = self.embeddings_model.encode(text, show_progress_bar=False)
            return embedding.tolist()
        except Exception as e:
            print(f"Embedding error: {e}")
            return []
    
    def extract_characters(self, text: str) -> Dict[str, Dict]:
        """
        Extract named entities (characters) from text.
        
        Args:
            text: Text to process
            
        Returns:
            Dict of character names and metadata
        """
        if not NLP_AVAILABLE:
            return {}
        
        try:
            self._ensure_nlp_model()
            doc = self.nlp_model(text)
            
            characters = {}
            for ent in doc.ents:
                if ent.label_ == 'PERSON':
                    name = ent.text
                    if name not in characters:
                        characters[name] = {
                            'name': name,
                            'mention_count': 0,
                            'description': '',
                        }
                    characters[name]['mention_count'] += 1
            
            return characters
        except Exception as e:
            print(f"Character extraction error: {e}")
            return {}
    
    def classify_content(self, text: str, labels: List[str]) -> Dict[str, float]:
        """
        Zero-shot classification of content.
        
        Args:
            text: Text to classify
            labels: Labels to classify into
            
        Returns:
            Dict of label -> confidence scores
        """
        if not SUMMARIZER_AVAILABLE:
            return {label: 0.0 for label in labels}
        
        try:
            classifier = pipeline('zero-shot-classification', 
                                 model='facebook/bart-large-mnli',
                                 device=-1)
            result = classifier(text, labels, multi_class=True)
            
            return dict(zip(result['labels'], result['scores']))
        except Exception as e:
            print(f"Classification error: {e}")
            return {label: 0.0 for label in labels}
    
    def calculate_readability(self, text: str) -> Dict[str, float]:
        """
        Calculate readability metrics.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dict with readability scores
        """
        try:
            return {
                'flesch_kincaid_grade': textstat.flesch_kincaid_grade(text),
                'flesch_reading_ease': textstat.flesch_reading_ease(text),
                'smog_index': textstat.smog_index(text),
                'gunning_fog': textstat.gunning_fog(text),
            }
        except Exception as e:
            print(f"Readability calculation error: {e}")
            return {}
    
    def find_similar_chapters(self, query_embedding: List[float], 
                             all_embeddings: List[List[float]], 
                             top_k: int = 5) -> List[int]:
        """
        Find similar chapters using embeddings (requires FAISS).
        
        Args:
            query_embedding: Query embedding vector
            all_embeddings: List of all chapter embeddings
            top_k: Number of similar chapters to return
            
        Returns:
            List of chapter indices
        """
        if not EMBEDDINGS_AVAILABLE or not query_embedding:
            return []
        
        try:
            import faiss
            
            # Convert to numpy array
            query_array = np.array([query_embedding]).astype('float32')
            embeddings_array = np.array(all_embeddings).astype('float32')
            
            # Create FAISS index
            dimension = embeddings_array.shape[1]
            index = faiss.IndexFlatL2(dimension)
            index.add(embeddings_array)
            
            # Search
            distances, indices = index.search(query_array, min(top_k, len(all_embeddings)))
            
            return indices[0].tolist()
        except Exception as e:
            print(f"Similarity search error: {e}")
            return []


# Global AI features instance
ai_features = AIFeatures()
