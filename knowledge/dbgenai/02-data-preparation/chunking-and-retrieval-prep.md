# Preparing documents for retrieval

**Domain:** dbgenai-02 — Task 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8
**Verified:** 2026-11-03
**Concepts:** chunking, chunk overlap, semantic chunking, parent document retriever, re-ranking, recall@k, precision@k, ndcg, mrr, delta lake, change data feed

> Seed note. Scope is from the official exam guide; deepen the extraction-library and
> metric detail from the linked docs before sealing hard items.

## Why this is on the exam

14% of the exam. Retrieval quality is decided here, before a single token is generated
— which is why "improve the prompt" is so often the wrong answer to a bad-answer
scenario.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 2.1 | Apply a chunking strategy for a given document structure and model constraints |
| 2.2 | Filter extraneous content in source documents that degrades quality of a RAG application |
| 2.3 | Choose the appropriate Python package to extract document content from provided source data and format |
| 2.4 | Define operations and sequence to write given chunked text into Delta Lake tables in Unity Catalog |
| 2.5 | Identify needed source documents that provide necessary knowledge and quality for a given RAG application |
| 2.6 | Use tools and metrics to evaluate retrieval performance |
| 2.7 | Design retrieval systems using advanced chunking strategies |
| 2.8 | Explain the role of re-ranking in the information retrieval process |

## Choosing a chunking strategy

| Document shape | Strategy |
|---|---|
| Long flowing prose | Fixed-size chunks with overlap, so a sentence split across a boundary is still recoverable |
| Clear structure (headings, sections, clauses) | Split on the structure, so a chunk is a coherent unit |
| Short records already self-contained (FAQ, product rows) | One chunk per record |
| Answers need local detail but wider context to make sense | Retrieve small chunks, return the larger parent passage |

Two constraints bound every choice: the **embedding model's** maximum sequence length,
and the **generator's** context window once you add the retrieved chunks to the prompt.

## Retrieval metrics

| Metric | Answers |
|---|---|
| **Recall@k** | Did the relevant chunk make it into the top k at all? |
| **Precision@k** | How much of the top k was actually relevant? |
| **MRR** | How high up was the first relevant result? |
| **NDCG** | Are the most relevant results ranked above the merely relevant ones? |

**Re-ranking** is a second scoring pass over the first-stage candidates. It cannot
rescue a chunk the retriever never returned — so it fixes *ordering* problems, not
*recall* problems. That distinction is the usual trap.

## Traps

- **Trap:** raising `k` to fix a bad answer. More chunks means more noise and a fuller
  context window; if recall was already fine, this makes things worse.
- **Trap:** re-ranking offered as the fix for a low recall@k. Fix retrieval first.
- **Trap:** leaving headers, footers, navigation and boilerplate in the corpus. They
  embed as plausible text and pollute the top k.
- **Trap:** chunk overlap set so high that near-duplicate chunks crowd out the rest of
  the result set.

## Verify before sealing

- [RAG on Databricks](https://docs.databricks.com/aws/en/generative-ai/retrieval-augmented-generation)
- [Mosaic AI Vector Search](https://docs.databricks.com/aws/en/generative-ai/vector-search)
- [Agent evaluation](https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/)
