from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial","B",16)

text = [' Adderall is a mixture of amphetamine salts that was developed for treatment of attention deficit hyperactivity disorder. \n    --', ' The amphetamine salts in Adderall are closely related to methamphetamine, and Adderall is a stimulant. When Adderall is ingested, it takes effect on the brain within an hour of use. \n    --', ' Adderall increases the effect of serotonin and dopamine in patients with ADHD, whose brain is constantly seeking out stimulants. \n    --', ' Adderall essentially tricks the brain into releasing more dopamine and serotonin, making the user feel more focused and alert. \n    --', " Adderall helped students without ADHD improve their grades in the short term, but it didn't help their academic performance in the long term. \n    --", ' In the third round, participants were given ten milligrams of Adderall, but were told it was a placebo. Finally, they were given a placebo and told it was a placebo. The groups that did the best were those who thought they had taken Adderall, regardless of whether they had or not\n    --', ' In fact, the group that did the worst were those who took Adderall but was told it was placebo. \n    --', ' Adderall is similar to meth in chemical structure and is also addictive. \n    --', ' The long-term effects of Adderall use include the inability to feel pleasure without a chemical stimulant, as well as the risk of developing addiction. \n    --', ' Adderall is an addictive drug. As a society, we need to put measures in place to protect people. \n    --', " If you're looking for study tips and advice, check out our videos about scientific study tips and advice! \n    --", " We'll put some more videos below. Make sure you're subscribed for a new video next Thursday.\n    \n     End of passage 1.\n\n===Visualization===\n\nThe user interface for explaining the Passage-Agnostic Word Embedding (PAVE) model. In the PAVE user interface, a PAVE word embedding is first initialized", ' Bye. \n    --']
for i in text:
    pdf.write(4," ")
    pdf.write(8, i +"HI")

pdf.output("creating-pdfs/Hi.pdf")