# =================================================================================
# Utility Script: Programmatic Export to .docx
# =================================================================================
#
# PURPOSE:
# This script provides a method to programmatically convert the main Jupyter Notebook
# into a .docx file.
#
# INSTRUCTIONS:
# To use this, you can copy and paste the active code (the lines without a '#'
# in front) into a new cell at the end of your Jupyter Notebook and run it.
#
# DEPENDENCIES:
# NOTE: This script requires 'pypandoc' to be installed (`%pip install pypandoc`)
# and a separate, system-level installation of the Pandoc application.
#
# --- QUALITY WARNING ---
# The direct conversion to .docx often has formatting issues with complex plots
# and the custom styled HTML headers used in this notebook.
#
# For the highest quality document, the recommended method is to export the
# notebook to HTML useing - !jupyter nbconvert --to html "Week4_Kaggle_BBC_News_Classification.ipynb" -
# open that HTML file in Microsoft Word, and then "Save As" a .docx file.
#
# --- !! USEFUL SIDE EFFECT !! ---
# A major benefit of running the first step of this script (the conversion to
# Markdown) is that `nbconvert` will automatically save all the plots from your
# notebook as individual .png files in a separate folder. This is a huge
# time-saver compared to manually saving each plot one by one.
#
# =================================================================================

# --- Dependency Installation & Version Checks ---
# Uncomment the line below if nbconvert is missing or needs an update.
# %pip install nbconvert

# Uncomment the line below if you need to install pandoc
# %pip install pypandoc

# Check your versions.
!jupyter nbconvert --version
!pandoc --version

# 

import subprocess
import pypandoc
import os

# --- Define Filenames ---
notebook_filename_in = "Week4_Kaggle_BBC_News_Classification.ipynb"
# nbconvert will automatically create the markdown file with the same base name
intermediate_md_file = notebook_filename_in.replace(".ipynb", ".md") 
output_docx_file = notebook_filename_in.replace(".ipynb", ".docx")


# --- Step A: Convert .ipynb to Markdown using nbconvert ---
print(f"--- Step 1/2: Converting '{notebook_filename_in}' to Markdown... ---")
try:
    subprocess.run(
        ['jupyter', 'nbconvert', '--to', 'markdown', notebook_filename_in],
        check=True, capture_output=True, text=True, encoding='utf-8'
    )
    print(" Successfully converted to Markdown.")
except subprocess.CalledProcessError as e:
    print("---  Conversion to Markdown Failed ---")
    print(e.stderr)


# --- Step B: Convert Markdown to .docx using pypandoc ---
if os.path.exists(intermediate_md_file):
    print(f"\n--- Step 2/2: Converting '{intermediate_md_file}' to .docx... ---")
    try:
        # pypandoc calls the pandoc executable you have installed
        pypandoc.convert_file(intermediate_md_file, 'docx', outputfile=output_docx_file)
        
        save_path = os.path.abspath(output_docx_file)
        print(f" Success! File saved to: {save_path}")

    except Exception as e:
        print("---  Conversion to .docx Failed ---")
        print(e)
    finally:
        # Clean up the intermediate markdown file
        if os.path.exists(intermediate_md_file):
            os.remove(intermediate_md_file)