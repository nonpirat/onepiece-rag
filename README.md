# One piece RAG
One piece chatbot using RAG with OpenAI embeddings and gpt-3.5-turbo

## Retrieval
| Model | Recall_1 | Recall_2 | Recall_5 | Recall_10 |
| ----- | ----- | ----- | ----- | ----- |
| BM25 | 0.490 | 0.577 | 0.694 | 0.767 |
| infloat/e5-base-v2 | 0.510 | 0.641 | 0.770 | 0.848 |
| Hybrid search | 0.555 | 0.692 | 0.829 | 0.893 |

The dataset contains 1500 pairs of queries and passages.