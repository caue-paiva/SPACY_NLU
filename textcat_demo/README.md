## Comentário projeto

Esse repo usa a library de NLP spacy para criar um modelo simples de classificação de texto para rotear entre várias chains e ferramentas de uma aplicação com LLMs

O modelo de linguagem é algo similar com o bag of words porém implementado com a arquitetura do Spacy 

## project.YML

Esse arquivo de YML é a arquitetura em High level do seu projeto de ML, setando coisas como treinamento em GPU/CPI, qual seram os dados de treinamento e teste, quais os arquivos de configuração do modelo.

Nesse arquivo também estão listados os nomes do comandos para converter, treinar , fazer avaliação e fazer package do modelo agora pronto

## /training2
Esse folder contem os 2 modelos atuais do spacy, o model-best (melhor modelo treinado até agora) e o model-last (ultimo modelo treinado)






<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo Textcat (Text Classification)

A minimal demo textcat project for spaCy v3. The demo data comes from the [tutorials/textcat_docs_issues](https://github.com/explosion/projects/tree/v3/tutorials/textcat_docs_issues) project.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `convert` | Convert the data to spaCy's binary format |
| `train` | Train the textcat model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model as a pip package |
| `visualize-model` | Visualize the model's output interactively using Streamlit |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` &rarr; `train` &rarr; `evaluate` &rarr; `package` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/docs_issues_training.jsonl`](assets/docs_issues_training.jsonl) | Local | Demo training data |
| [`assets/docs_issues_eval.jsonl`](assets/docs_issues_eval.jsonl) | Local | Demo development data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
