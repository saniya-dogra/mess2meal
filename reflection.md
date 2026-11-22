# Mess2Meal — development reflection draft

> **This is a draft about the software-building process, based on the work recorded in this repository conversation. It is not a personal fieldwork reflection.** Before submitting, rewrite it in your own voice and add what actually happened during your visit, interview and data collection. Do not claim experiences that did not happen.

## What I learned while building the prototype

At the beginning, it was tempting to treat the problem as simply collecting leftover food and finding an NGO. While developing the project, I realised that a useful workflow needs more than a food listing. It needs information such as the food source, quantity, preparation time, best-before time, storage description and pickup location. The recipient side also needs details such as food preferences, capacity and whether it is currently accepting donations.

The project scope needed to be realistic. A matching algorithm can shortlist recipients using category, capacity and urgency, but it cannot decide whether food is safe to eat. That requires appropriate human checks and safe handling. For this reason, the documentation now makes clear that a suggested match is not a confirmed donation or a food-safety certificate.

AI assistance was useful for structuring the Python application, drafting FastAPI and Streamlit components, preparing test cases, creating Mermaid diagrams and improving the README. It also helped generate example CSV rows for testing the dashboard. However, generated examples could easily be mistaken for real research data if they were not labeled clearly. I therefore kept the sample rows marked as synthetic and documented that they must not be counted as fieldwork.

A key limitation of the current prototype is that it is still a local demonstration. It does not automatically contact NGOs, arrange transport, verify recipients or certify food. The next important improvement should be based on the actual workflow observed at a mess or restaurant rather than adding features based only on assumptions.

## Add your own fieldwork reflection before submission
Write one or two paragraphs in your own words answering:
1. What did you initially misunderstand about the surplus-food problem?
2. What did the person you interviewed actually tell you?
3. What did you observe that changed your assumptions?
4. Which feature would you remove or simplify after seeing the real workflow?
5. What did AI get wrong or assume, and how did you correct it?
6. What would you build next based on the evidence you collected?

**Do not submit this draft unchanged as a reflection of a visit or interview.**
