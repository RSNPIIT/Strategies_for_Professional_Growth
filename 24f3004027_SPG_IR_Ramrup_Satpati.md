# Interim Report – Qualitative Findings
**Beyond Quick Fixes: Diagnosing Technical Debt & Developer Burnout Through Systems Thinking**  
**Course:** Strategies for Professional Growth (BSGN3001) | **Team:** 114 – ITERATE | **Interviewer:** Ramrup Satpati  

---

### 1. External Participant
**Shubham Mishra** is a Computer Vision and Full-Stack Software Engineer at Siemens with about 3 years of industry experience. Concurrently pursuing the Diploma level in the IIT Madras BS Degree Programme, he is a recognized Project Topper across multiple Diploma projects and leads the educational community **LazyIITians**, providing mentoring and coaching for Diploma-level subjects in the IITM BS curriculum. His professional domain spans deep learning vision pipelines, full-stack API architectures, and real-time inference optimization under strict latency SLAs, offering unique dual insights into industrial deadline pressures, academic project excellence, black-box legacy debt, developer burnout, and engineering–leadership alignment.

---

### 2. Key Interview Questions and Discussion Points

| Finding | Timestamp | Key interview question / discussion prompt |
| :--- | :---: | :--- |
| **1. Architectural Shortcuts & Logic Bypass** | **00:35** | Can you walk me through a project where tight deadlines forced shortcuts? What was cut and what was the immediate payoff? |
| **2. Initial Payoff vs. Delayed Defects** | **01:15** | What happened in the weeks following that release when subsequent feature requests and edge-case bug fixes arrived? |
| **3. Production Firefighting & Stability** | **01:50** | What was the day-to-day reality of maintaining that system in production? How did rollbacks and missing tests affect routine operations? |
| **4. Developer Fatigue & Black-Box Code** | **02:30** | How did persistent operational firefighting impact developer well-being, morale, and willingness to modify legacy modules? |
| **5. The Refactoring Deferral Dilemma** | **03:10** | Did the team attempt to push back or request cleanup sprints in standups/retros? How did product management respond? |
| **6. Engineering–Leadership Dialogue Gap** | **03:55** | Why do technical debt concerns often stall with leadership? How can engineers reframe code quality into business priorities? |
| **7. Balanced Governance & Token Allocation** | **04:35** | How did your team ultimately align with product managers to reserve sprint capacity specifically for debt remediation? |
| **8. High-Leverage Sustainable Practices** | **05:10** | What specific technical safety nets (e.g., CI/CD, Boy Scout rule) and cultural norms best break the cycle of recurring debt? |

---

### 3. Key Findings and Interpretations

| Finding | Timestamp | Summary / interpretation | Verbatim statement |
| :--- | :---: | :--- | :--- |
| **1. Architectural shortcuts & logic bypass** | **00:52** | To satisfy an urgent client demo, the team embedded business logic directly into API handlers, hardcoded configs, and skipped tests; immediate success legitimized the shortcut. | *“In a client demo, instead of building a proper service layer the team put business logic in API handlers... it worked, demo went well, and the shortcut felt like the right call.”* |
| **2. Initial payoff vs. delayed defects** | **01:28** | Immediate post-release bugs were patched rapidly, giving a false sense of security before cumulative architectural friction emerged during subsequent scaling. | *“It’s not very bad [at first], some bugs came but were almost instantaneously fixed in...”* |
| **3. Production firefighting & stability** | **02:08** | Production support degraded into chronic firefighting, emergency 'last Friday' rollbacks, and fragile band-aids without proper automated validation safety nets. | *“Maintain a production system caused lots of firefighting... 'last Friday' rollbacks... sat with one or two people and cleared messy parts in favor of 'something that works'.”* |
| **4. Developer fatigue & black-box code** | **02:44** | Constant emergency firefighting led to severe developer burnout and an organizational fear of touching legacy code, turning critical modules into black boxes. | *“Couple of good developers were clearly burnt out... Over time people grew not to touch certain files, like a black box.”* |
| **5. Refactoring deferral dilemma** | **03:25** | Engineers repeatedly raised architectural degradation in standups and retros, but customer feature pressure consistently kicked remediation into a 'next sprint' that never arrived. | *“The pressure to keep shipping does take over... cleanup kept happening to the next sprint, and the next sprint just never came.”* |
| **6. Engineering–leadership dialogue gap** | **04:12** | Engineers framed debt as 'poor code quality', whereas leadership prioritized delivery speed and client impact; aligning required translating technical risk into business metrics. | *“Part of the problem was on our side... leadership cares about delivery speed, customer ease, impact, and satisfaction, and we were not speaking that language.”* |
| **7. Balanced governance & capacity** | **04:48** | Achieving transparency enabled product managers to formally allocate a percentage of sprint tokens/tickets specifically for technical debt remediation and downtime prevention. | *“Engineers need to make technical debt measurable and connect it to a business outcome... PM agreed on tickets and tokens reserved at some percentage.”* |
| **8. High-leverage sustainable practices** | **05:25** | Combining continuous hygiene (Boy Scout rule, CI/CD safety nets, peer reviews) with cultural psychological safety creates resilient and sustainable engineering workflows. | *“Follow the Boy Scout rule... CI/CD pipelines used as a safety net... keep code sustainable, share knowledge with peers, and provide psychological safety.”* |

---

### 4. Personal Reflection, Observations and Learning
This interview vividly grounded Peter Senge's (1990) Systems Thinking archetypes in high-stakes software engineering. The decision to bypass a formal service layer and hardcode configs to meet an urgent client demo exemplifies the *'Fixes that Fail'* archetype: the quick fix delivered immediate operational success, yet triggered severe delayed blowbacks in the form of 'last Friday' emergency rollbacks and unvalidated production patches. Over time, symptomatic workarounds substituted for foundational architecture, instantiating *'Shifting the Burden'* and degrading team capability into a state where engineers feared touching critical code, treating key modules as unmaintainable 'black boxes'.

Critically, the participant uncovered the missing link in our conceptual causal loop diagram: the breakdown of the human balancing loop. While our model assumed that developer fatigue would naturally prompt organizational pushback, the interview revealed that refactoring requests stall when engineers describe debt purely as 'poor code quality'—an internal technical concern. Leadership operates on delivery velocity, customer satisfaction, and business impact. The balancing loop only activated when the team translated technical liability into measurable business outcomes, enabling product managers to formalize reserved capacity (sprint token allocations) for debt reduction.

Finally, this interaction reinforced SPG Week 11's core principle of *Engineering Sense*. Sustainable velocity is not achieved by dogmatically rejecting shortcuts, but by establishing robust safety nets—continuous integration (CI/CD), rigorous code reviews, the Boy Scout rule ('leave code cleaner than you found it'), and psychological safety where developers can openly discuss trade-offs. True engineering excellence requires mastering both socio-technical dimensions: building disciplined automated technical barriers while actively communicating across organizational hierarchies in business-aligned terms.
