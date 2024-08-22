import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

# Function to generate resume PDF
def generate_resume():
    # Collect input data
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()
    summary = summary_text.get("1.0", tk.END).strip()
    skills = skills_text.get("1.0", tk.END).strip().split(',')
    experience = experience_text.get("1.0", tk.END).strip()
    education = education_text.get("1.0", tk.END).strip()
    projects = projects_text.get("1.0", tk.END).strip()
    
    # Check if all required fields are filled
    if not name or not phone or not email or not address:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return
    
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Add contact information
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=name, ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Address: {address}", ln=True, align='C')
    pdf.ln(10)
    
    # Add summary
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.ln(5)
    
    # Add skills
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ", ".join(skills))
    pdf.ln(5)
    
    # Add experience
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, experience)
    pdf.ln(5)
    
    # Add education
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, education)
    pdf.ln(5)
    
    # Add projects
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Projects", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, projects)
    pdf.ln(5)
    
    # Save PDF
    pdf.output("resume.pdf")
    
    messagebox.showinfo("Success", "Resume created successfully!")

# Create the main window
root = tk.Tk()
root.title("Resume Generator")

# Define variables for storing user input
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()

# Create labels and entry widgets for user input
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=name_var, width=50).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=phone_var, width=50).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=email_var, width=50).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=address_var, width=50).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Summary:").grid(row=4, column=0, padx=10, pady=5, sticky="ne")
summary_text = tk.Text(root, width=50, height=4)
summary_text.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Skills (comma-separated):").grid(row=5, column=0, padx=10, pady=5, sticky="ne")
skills_text = tk.Text(root, width=50, height=4)
skills_text.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Experience:").grid(row=6, column=0, padx=10, pady=5, sticky="ne")
experience_text = tk.Text(root, width=50, height=4)
experience_text.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Education:").grid(row=7, column=0, padx=10, pady=5, sticky="ne")
education_text = tk.Text(root, width=50, height=4)
education_text.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Projects:").grid(row=8, column=0, padx=10, pady=5, sticky="ne")
projects_text = tk.Text(root, width=50, height=4)
projects_text.grid(row=8, column=1, padx=10, pady=5)

# Create a button to generate the resume
tk.Button(root, text="Generate Resume", command=generate_resume).grid(row=9, column=1, pady=20)

# Start the Tkinter main loop
root.mainloop()
