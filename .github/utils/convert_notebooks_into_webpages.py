import re

from nbconvert import MarkdownExporter
import os
from pathlib import Path

headers = {
    1: """<!---
title: "Tutorial 1"
metaTitle: "Build Your First QA System"
metaDescription: ""
slug: "/docs/tutorial1"
date: "2020-09-03"
id: "tutorial1md"
--->""",
    2: """<!---
title: "Tutorial 2"
metaTitle: "Fine-tuning a model on your own data"
metaDescription: ""
slug: "/docs/tutorial2"
date: "2020-09-03"
id: "tutorial2md"
--->""",
    3: """<!---
title: "Tutorial 3"
metaTitle: "Build a QA System Without Elasticsearch"
metaDescription: ""
slug: "/docs/tutorial3"
date: "2020-09-03"
id: "tutorial3md"
--->""",
    4: """<!---
title: "Tutorial 4"
metaTitle: "Utilizing existing FAQs for Question Answering"
metaDescription: ""
slug: "/docs/tutorial4"
date: "2020-09-03"
id: "tutorial4md"
--->""",
    5: """<!---
title: "Tutorial 5"
metaTitle: "Evaluation of a QA System"
metaDescription: ""
slug: "/docs/tutorial5"
date: "2020-09-03"
id: "tutorial5md"
--->""",
    6: """<!---
title: "Tutorial 6"
metaTitle: "Better retrieval via Dense Passage Retrieval"
metaDescription: ""
slug: "/docs/tutorial6"
date: "2020-09-03"
id: "tutorial6md"
--->""",
    7: """<!---
title: "Tutorial 7"
metaTitle: "Generative QA with RAG"
metaDescription: ""
slug: "/docs/tutorial7"
date: "2020-11-12"
id: "tutorial7md"
--->""",
    8: """<!---
title: "Tutorial 8"
metaTitle: "Preprocessing"
metaDescription: ""
slug: "/docs/tutorial8"
date: "2021-01-08"
id: "tutorial8md"
--->""",
    9: """<!---
title: "Tutorial 9"
metaTitle: "Training a Dense Passage Retrieval model"
metaDescription: ""
slug: "/docs/tutorial9"
date: "2021-01-08"
id: "tutorial9md"
--->""",
    10: """<!---
title: "Tutorial 10"
metaTitle: "Knowledge Graph QA"
metaDescription: ""
slug: "/docs/tutorial10"
date: "2021-04-06"
id: "tutorial10md"
--->""",
    11: """<!---
title: "Tutorial 11"
metaTitle: "Pipelines"
metaDescription: ""
slug: "/docs/tutorial11"
date: "2021-04-06"
id: "tutorial11md"
--->""",
    12: """<!---
title: "Tutorial 12"
metaTitle: "Generative QA with LFQA"
metaDescription: ""
slug: "/docs/tutorial12"
date: "2021-04-06"
id: "tutorial12md"
--->""",
    13: """<!---
title: "Tutorial 13"
metaTitle: "Question Generation"
metaDescription: ""
slug: "/docs/tutorial13"
date: "2021-08-23"
id: "tutorial13md"
--->""",
    14: """<!---
title: "Tutorial 14"
metaTitle: "Query Classifier Tutorial"
metaDescription: ""
slug: "/docs/tutorial14"
date: "2021-08-23"
id: "tutorial14md"
--->""",
    15: """<!---
title: "Tutorial 15"
metaTitle: "TableQA Tutorial"
metaDescription: ""
slug: "/docs/tutorial15"
date: "2021-10-28"
id: "tutorial15md"
--->""",
    16: """<!---
title: "Tutorial 16"
metaTitle: "DocumentClassifier at Index Time Tutorial"
metaDescription: ""
slug: "/docs/tutorial16"
date: "2021-11-05"
id: "tutorial16md"
--->""",
}


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    test = [atoi(c) for c in re.split("(\d+)", text)]
    return test


dir = Path(__file__).parent.parent.parent / "tutorials"

notebooks = [x for x in os.listdir(dir) if x[-6:] == ".ipynb"]
# sort notebooks based on numbers within name of notebook
notebooks = sorted(notebooks, key=lambda x: natural_keys(x))


e = MarkdownExporter(exclude_output=True)
for i, nb in enumerate(notebooks):
    body, resources = e.from_filename(dir / nb)
    print(f"Processing {dir}/{nb}")

    tutorials_path = Path(__file__).parent.parent.parent / "docs" / "_src" / "tutorials" / "tutorials"
    with open(tutorials_path / f"{i + 1}.md", "w", encoding="utf-8") as f:
        f.write(headers[i + 1] + "\n\n")
        f.write(body)
