#!/usr/bin/env python3
import json
from pathlib import Path

NARRATIVES = {
    "1037798": {
        "1": "Relevant passages contain information about the US history where only the name Robert Gray is mentioned (e.g., exploration of Columbia River, province of British Columbia). Non relevant passages are are usually header or footer chunks or just paragraphs that are unrelated to the query but contain the keyword “Robert Gray” (e.g., Bruno Heceta for Spain in 1775, the American Capt. Robert Gray in 1792, and Capt. George Vancouver for Britain in 1792–1794.). Perfectly relevant are passages with information regaring the accomplishments of Robert Gray on his sailing vessel and his discoveries and hightly relevant are similar but hidden amongst extraneous unrelated information.",
        "2": "I'm at a maritime museum and a plaque mentioned the name Robert Gray. It didn't give much context, so I want to learn more about him. A perfectly relevant passage is one dedicated to Robert Gray, covering main details about him and what he's known for. A relevant passage gives some details about Robert Gray (nationality, profession, etc.). A related passage only mentions Robert Gray, but doesn't give any details. All other content is non-relevant."
    },
    "1106007": {
        "1": """A passage is perfectly relevant if it provides a direct and comprehensive definition of the term "visceral" in its various contexts. This includes explaining its primary meaning related to internal organs or gut feelings, as well as its figurative use to describe instinctive or emotional reactions. If the passage provides a definition of "visceral" but lacks some depth or context, it is considered highly relevant. The passage is considered relevant if it mentions "visceral" in a context that hints at its meaning without providing a direct definition. If the passage does not mention "visceral" at all or uses it in a way that doesn't contribute to understanding its definition, it is considered not relevant.""",
        "2": """I'm an English language learner and I encountered the term visceral. Relevant passages should provide a clear and concise definition. A perfectly relevant passage should provide a direct definition. A relevant passage will provide a definition but does not focus on it. A related passage provides other information about the word (e.g., etymology). All other content is non-relevant."""
    },
    "443396": {
        "1": """A passage is perfectly relevant if it directly defines or explains the LPS Act, its purpose, and its key components. If the passage provides information closely related to the LPS Act but doesn't directly define it, it is considered highly relevant. This may include passages that discuss similar laws in other states, explain procedures related to involuntary commitment, or provide details about the implementation of such laws. The passage is considered relevant if it touches on topics related to mental health laws, involuntary commitment, or conservatorship, but doesn't specifically focus on the LPS Act or provide a direct definition. If the passage contains information about legal or medical topics that are not directly related to mental health laws or involuntary commitment, it is considered not relevant.""",
        "2": """I'm applying to law schools and trying to figure out what area to specialize in. I saw the term "LPS Law" somewhere and I want to know what it is. Since I do not already know what "LPS Law" is, relevant documents should mention LPS specifically, rather than describing examples of LPS laws such as Flordia's Baker Act (without directly linking it to LPS). A perfectly relevant passage provides a clear and direct definition of LPS law. A relevant passage provides an incomplete or otherwise hidden definition of LPS law. A related passage will cover other related topics such as LPS conservatorships. All other content is non-relevant."""
    }
}

USER_TO_NARRATIVE = {
    "andrew-parry": "2",
    "eugene-yang": "1",
    "ferdinand-schlatt": "2",
    "froebe": "1",
    "guglielmo-faggioli": "2",
    "harry-scells": "1",
    "saber-zerhoudi": "2",
    "sean-macavaney": "1"
}

for user, narrative in USER_TO_NARRATIVE.items():
    lines = []
    with open('query-doc-pools.jsonl', 'r') as f:
        for l in f:
            lines.append(json.loads(l))

    Path('doccano').mkdir(exist_ok=True)
    with open(f'doccano/{user}-narrative-study.jsonl', 'w') as f:
        for l in lines:
            l['narrative'] = NARRATIVES[l['query_id']][narrative]
            l['label'] = []
            f.write(json.dumps(l) + '\n')


