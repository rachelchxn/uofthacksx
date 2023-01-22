from fpdf import *

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('front-end/images/logo.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Times', 'B', 15)
        # Move to the right
        self.cell(50)
        # Title
        self.cell(100, 10, 'Condensed Notes on Video', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.set_x(150)
        #date
        self.cell(80, 10, 'Data Generated: 01/22/22', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

textsorted = [['definition', 'Our bodies run on energy. Even as you sit watching this, your body is generating enough energy to power 710 watt light bulbs. Most of that energy is provided by tiny structures called mitochondria present inside our cells.'], ['definition', "These mitochondria are the powerhouses of a human body. They take fat, sugar, and protein from our food and combine it with oxygen oxygen, converting it into energy for our cells and tissues such as brain and muscle, mitochondria have their own DNA that's crucial to this energy conversion process."], ['point', 'This is different to the DNA found in the nucleus. While nuclear DNA determines our physical characteristics, mitochondrial DNA does not. But both types of DNA must be healthy for the mitochondria to function effectively.'], ['example', 'Faults in either can cause mitochondria to stop working properly, preventing them from converting fuel into energy.'], ['point', 'If the number of 40 mitochondria reaches a critical level, our cells begin to run out of energy, fail, and even die. Since mitochondria performs so many different functions, there are literally hundreds of different mitochondrial diseases.'], ['point', 'The effects include fatigue, speech disorders, hearing difficulties, muscle weakness, heart problems, liver disease, bowel problems, and sometimes, in very severe cases, it may even be fatal.'], ['point', "The sheer variety of symptoms associated with mitochondrial disease makes it hard to diagnose. Despite this, we're making rapid advances every day in our understanding of how it develops and is passed on. All of which help us to devise new strategies to prevent and treat the disease in the future."], ['main concept', 'To learn more about mitochondrial disease, please visit our website.'], ['example', ' Our bodies run on energy. Even as you sit watching this, your body is generating enough energy to power 710 watt light bulbs. Most of that energy is provided by tiny structures called mitochondria present inside our cells. \n    --'], ['definition', " Mitochondria take fat, sugar, and protein from our food and combine it with oxygen, converting it into energy for our cells and tissues such as brain and muscle. Mitochondria have their own DNA that's crucial to this energy conversion process. This is different to the DNA found in the nucleus. \n    --"], ['example', ' Faults in either type of DNA can cause mitochondria to stop working properly, preventing them from converting fuel into energy. \n    --'], ['point', ' If the number of 40 mitochondria reaches a critical level, our cells run out of energy, fail, and even die. There are literally hundreds of different mitochondrial diseases. The effects include fatigue, speech disorders, hearing difficulties, muscle weakness, heart problems, liver disease, bowel problems, and sometimes, in very severe cases, it may even be fatal. \n    --'], ['main concept', ' Mitochondrial disease is hard to diagnose, but new research helps us understand it better, which helps us devise new treatments\n    --'], ['main concept', ' To learn more about mitochondrial disease, please visit our website. \n    --']]
keywords = [' Mitochondria\n    --']

count = 0 

pdf.write(8,"List of Key Concepts Covered in this video:")
    
for i in range(len(keywords)):
    pdf.write(8,keywords[i])
        

pdf.write(8,"\n")

for i in range(len(textsorted)):
    
    if textsorted[i][0] == 'definition':
        pdf.set_font('Arial', 'B', 12)
        count += 1
        pdf.write(8, "Definition #" +str(count)+ "\n")
        
    elif textsorted[i][0] == "example":
        pdf.set_font('Times', '', 12)
        pdf.write(8, " -----> Ex: ")
    
    elif textsorted[i][0] == "main concept":
        pdf.set_font('Times', 'B', 12)
        pdf.write(8,"Core Concept: ")
        pdf.write(8,"\n")
        
    elif textsorted[i][0] == "point":
        pdf.set_font('Times', '', 12)
        pdf.write(8,"      Point: ")
        
    pdf.write(8,textsorted[i][1])
    pdf.write(8,"\n")
    pdf.write(8,"\n")
    
pdf.output("creating-pdfs/tldr.pdf")
