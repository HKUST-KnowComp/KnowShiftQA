# KnowShiftQA: How Robust are RAG Systems when Textbook Knowledge Shifts in K-12 Education?

Official Github Repository for ACL 2025 paper:<br> *KnowShiftQA: How Robust are RAG Systems when Textbook Knowledge Shifts in K-12 Education?*  [![arXiv](https://img.shields.io/badge/arXiv-2412.08985-B31B1B.svg)](https://arxiv.org/pdf/2412.08985)


## 📚 Overview

KnowShiftQA is a novel question answering dataset designed to systematically evaluate the robustness of Retrieval-Augmented Generation (RAG) systems when faced with knowledge discrepancies between textbooks and Large Language Models (LLMs) in K-12 education.

The dataset simulates real-world scenarios where textbook knowledge differs from LLMs' parametric knowledge through deliberate hypothetical knowledge updates, reflecting how educational content can shift due to evolving facts, pedagogical updates, or regional variations.

## 🎯 Key Features

- **3,005 multiple-choice questions** across 5 subjects (Physics, Chemistry, Biology, Geography, History)
- **Comprehensive question typology** focusing on context utilization and knowledge integration
- **Hypothetical knowledge updates** that maintain coherent and consistent contexts
- **Systematic evaluation** of both retrieval methods and LLM performance

## 📊 Dataset Statistics

### Subject Distribution
| Subject | # Questions | # Documents | Avg Doc Length |
|---------|------------|-------------|----------------|
| Chemistry | 347 | 291 | 315.5 |
| Biology | 873 | 671 | 588.1 |
| Physics | 224 | 166 | 647.3 |
| Geography | 690 | 471 | 429.8 |
| History | 871 | 606 | 277.1 |
| **Total** | **3,005** | **2,205** | **437.3** |

### Question Types
| Question Type | Count | Description |
|--------------|-------|-------------|
| Simple Direct | 610 | Direct factual queries |
| Multi-hop Direct | 655 | Multi-step reasoning with explicit facts |
| Multi-hop Distant | 708 | Multi-step reasoning with distant facts |
| Multi-hop Implicit | 417 | Integration of contextual and parametric knowledge |
| Distant Implicit | 615 | Combined challenge of distant facts and knowledge integration |

## 🚀 Main Results

### Retrieval Performance
| Retrieval Method | Category | R@1 | R@5 |
|-----------------|----------|------|------|
| BM25 | Lexical | **82.73** | 95.27 |
| Ada-002 | Dense | 79.23 | 95.44 |
| Hybrid Rerank | Ensemble | 84.43 | 96.04 |
| Contriever-msmarco (fine-tuned) | Dense+FT | **87.95** | **99.50** |

### Question Answering Performance (Top Models)
| Model | Simple Direct | Multi-hop Direct | Multi-hop Distant | Multi-hop Implicit | Distant Implicit | Average |
|-------|--------------|------------------|-------------------|-------------------|------------------|---------|
| Llama3-8b | 90.33 | 88.85 | 89.69 | 63.55 | 49.43 | 77.77 |
| GPT-4-turbo | 95.74 | 96.18 | 96.19 | 81.06 | 71.71 | 88.99 |
| Claude-3.5-sonnet | 97.54 | 96.49 | 95.62 | 83.69 | 73.82 | 90.08 |
| o1-preview | 95.08 | **97.71** | **97.46** | **86.33** | **78.86** | **91.68** |

### RAG System Performance Drop
| RAG System | Before Update | After Update | Performance Drop |
|------------|---------------|--------------|------------------|
| Llama3-8b + Ada-002 | 87.49% | 62.60% | -24.89% |
| Llama3-8b + Rerank | 88.49% | 66.02% | -22.47% |
| GPT-4o + Ada-002 | 96.57% | 69.65% | -26.92% |
| GPT-4o + Rerank | 97.10% | 73.71% | -23.39% |

## 💡 Key Findings

1. **Substantial Performance Degradation**: RAG systems experience a 22-27% accuracy drop when facing knowledge discrepancies
2. **Knowledge Integration Challenge**: Questions requiring integration of contextual and parametric knowledge pose significant challenges, especially for smaller LLMs
3. **Retrieval Method Insights**: 
   - Lexical methods (BM25) perform competitively due to domain-specific terminology
   - Fine-tuning dense retrievers on domain data yields significant improvements
   - Ensemble methods can further enhance performance
