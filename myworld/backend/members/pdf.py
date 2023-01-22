from fpdf import *
import os



class PDF(FPDF):
    def header(self):
        # Logo
        # self.image('https://cdn.discordapp.com/attachments/1063103394958553108/1066635982704750722/Screen_Shot_2023-01-21_at_11.03.56_PM.png', 10, 8, 33)
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

def toPdf(sum_array, keywordList):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)

    textsorted = sum_array
    print('hEREEEEEEEEEEEEEEE: ', textsorted)
    # for i in sum_array:
    #     if sum_array[sum_array.index(i)][1][-1] == '-':
    #         add = sum_array[sum_array.index(i)][1][-1][1].removesuffix('--')
    #     else:
    #         add = sum_array[sum_array.index(i)][1][-1][1]

    #     textsorted.append([sum_array.index(i), add])

    keywords = keywordList

    count = 0 

    pdf.write(8,"Keywords in this video: ")
        
    for i in range(len(keywords)):
        pdf.write(8,keywords[i])
            

    pdf.write(8,"\n")
    pdf.write(8,"\n")

    for i in range(len(textsorted)):
        
        if textsorted[i][0] == 'Definition':
            pdf.set_font('Arial', 'B', 12)
            count += 1
            pdf.write(8, "Definition #" +str(count)+ "\n")
            
        elif textsorted[i][0] == "Example":
            pdf.set_font('Times', '', 12)
            pdf.write(8, " -----> Ex: ")
        
        elif textsorted[i][0] == "Core Concept":
            pdf.set_font('Times', 'B', 12)
            pdf.write(8,"Core Concept: ")
            pdf.write(8,"\n")
            
        elif textsorted[i][0] == "Point":
            pdf.set_font('Times', '', 12)
            pdf.write(8,"      Point: ")
            
        pdf.write(8,textsorted[i][1])
        pdf.write(8,"\n")
        
    pdf.output(r"C:\Users\rache\Documents\GitHub\uofthacksx\front-end\src\imgs\tldw.pdf")
