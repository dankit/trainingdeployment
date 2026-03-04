This was the custom torch elastic configuration i had to setup when training on preemptible gpus for the legal agentic RAG project, in which I attempted to train the reranker

All projects/artifacts/images that are referenced here are now defunct

Setup entails:
Google compute engine, and google kubernetes engine

1x durable rdzv server, with persistent storage for checkpoints (attached through pv/c)
1-3x preemptible gpus

