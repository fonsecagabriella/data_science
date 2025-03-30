# Visualisation: Diabetes Care Analytics

[Link to Tableau](https://public.tableau.com/app/profile/gabi.fonseca/viz/Diabetes_17429186215350/Sheet6#1)

## Background
You are a data analyst at MedInsight Solutions, a healthcare analytics consultancy helping hospitals improve patient outcomes. Your task is to identify factors influencing diabetes readmission rates and provide actionable recommendations to hospital administrators.

In this lab you will be working with a slightly pre-processed version of the 
[Diabetes 130-US Hospitals](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) dataset.


- Copy the data
- Define the relationships between the tables.  


## Exercise 2: Inspect the data
Create a new Worksheet

On the left side you should see all the tables. Take a moment to inspect the available data. You can drag some fields into the sheet to see what the dataset looks like

## Exercise 3: Creating New Fields
If you want to look into aggregated values of the “Readmitted” field, you will need to create new fields, because Tableau doesn’t know how to summarize the field

Create a new Calculated Field called "Not Readmitted”: 

Go to Analysis and select Create Calculated Field

Change the name from “Calculation1” to “Not Readmitted”

In the calculation box type the formula FLOAT([Readmitted]="NO"). Here is the breakdown of the formula: 

[Readmitted]="NO" returns a boolean. Note that the variable goes between square brackets

FLOAT() transforms the boolean to a float (1 or 0). This way, you can then aggregate the data by summing.

Repeat the process to create two more Calculated Fields:

“Readmitted >30”

“Readmitted <30”

To check your results, drag the fields “Age”, “Not Readmitted”, “Readmitted >30” and “Readmitted <30” into the sheet. This will show the number of patients in each age group with each type of readmission. 


## Exercise 4: Aggregated Charts
To improve the visualization of the relationship between the patient’s  age and whether they are readmitted or not, you decide to create a side-by-side bars chart

Create a new Worksheet and name it “Readmissions by Age”

You want the horizontal axis to show the age groups, so drag the “Age” field into Columns

The height of the columns should represent the number of each readmitted category, so drag the newly created fields “Not Readmitted”, “Readmitted >30” and “Readmitted <30” into Rows 


## Exercise 5: Aggregated Charts Continued
The previous chart is very insightful, but it is also very dependent on the number of patients in each age group. Another question that is worth answering is on what proportion are patients being readmitted before 30 days, after 30 days or aren’t readmitted at all

Copy the Workingsheet from the previous exercise. You can do this by right clicking on the tab, and selecting the Duplicate option.

Rename the new sheet as “Rate of Readmissions by Age”

Change the Measure of each Row to Average. To do this, you can right click on each of the fields in Measure Values, select Measure, and then Average.

## Exercise 6: Disaggregated Charts
Next, you decide to analyze the relationship between prior inpatient and outpatient visits. If patients with frequent outpatient care still require hospitalization, that could be revealing gaps in preventive management.

Create a new Worksheet and name it “Inpatient-Outpatient”

Drag the field “Number Inpatient” into Columns.

Drag the field “Number Outpatient” into Rows

To disaggregate the data, go to the Analysis menu, and deselect the option Aggregate Measures

Click on the Show Me button, and select the scatter plot


## Exercise 7: Improving a chart
You're interested in analyzing how readmission numbers vary across demographic groups to identify which patient populations may benefit from targeted discharge planning and follow-up care interventions. You will start by customizing the chart from Lesson 1 to better suit your needs:

Copy the “Readmissions by Age worksheet”

Remove Measure Names from Columns, so you get a stacked bar chart

Swap columns and rows. You can do this by clicking on the button swap button on the top bar

Change the legend title to “Readmissions”:  go to the legend box, and click on the black arrow next to the title. Select Edit Title…, and insert the new title

Change the color of the different categories. Use green for “Not Readmitted”, orange for “Readmitted >30”, and red for “Readmitted <30”. You can do this by clicking on the black arrow next to the legend title and this time select Edit Colors…

Allow highlighting by Readmission category: click on the highlighter button next to the legend title

Change the vertical axis label to “Number of Patients" 	

Set the title to “Number of Readmissions by Age Group”



## Exercise 8: Adding filters
Now you are ready to add the filters

Rename the tab from the previous exercise to “Readmissions by demographics”

In order to see data by gender, add the field “Gender” to Rows. This will split the bars into two for each age group

Now add the filter by “Race”. You can do this by dragging the field into Filters box

Make the filter visible: right click on the filter and select the Show Filter option

Next, add Mark Labels. For that, you can select the option from the Analysis menu

Having the marks active all the time is a bit overwhelming. You decide to only show the marks for the highlighted values only. 

Click on the Label box

From the Marks to Label dropdown menu select Highlighted. 

Tick the option Allow labels to overlap other marks. This way, you can still see the values of very small (or zero) categories

For example, if you select Asian, and highlight Not Readmitted.


## Exercise 9: Adding Data to Tooltips
You want to add information about the readmission rates into the Tooltips

Drag the fields “Not Readmitted”, “Readmitted >30” and “Readmitted <30” into Tooltip

Change the measure of each of the fields to Average (only in tooltip) 

Click on the Tooltip button, and edit the text to look like this: 

You can add the field calculation by selecting from the Insert dropdown menu

Select OK. Now you should see the more informative tooltip as you hover over the different segments in the chart

## Exercise 10: Pie Chart
You wish to know if receiving diabetes medication has any impact on the readmission of the patient

Create a new Worksheet and name it “Medication”

Drag the “Diabetes Med” field

Next, drag diabetes.csv (Count) to get how many patients are in each category. 

Drag the “Readmitted” field into Columns so segment the data by readmissions

Now you are ready to create the pie chart

After selecting the pie chart, you might see that “Readmitted” moved into Rows. If that happens, drag it back to Columns, so you get the 3 pie charts next to each other

Next, drag the “diabetes.csv (Count)” field into Label

To show the percentage instead of the count, right click on the CNT(diabetes.csv), and select Quick Calculation, and then click on Percentage of Total.  Make sure you are clicking on the one for labels.

This shows the percentage of the total number of patients, but you would like to know the percentage for each segment. Right click again on CNT(diabetes.csv), and this time go to Compute Using, and select Table (down)

Change the title to “Patients on Diabetes Medication for Each Readmission Type”

You should get something like this:


## Exercise 11: Treemaps
You want to analyze the distribution of primary diagnoses among diabetes patients to identify which comorbidities are most prevalent and how they correlate with readmission outcomes. In particular, you are interested in identifying diseases with high readmission before 30 days. You will be doing this with a treemap chart

Create a new Worksheet and name it Diagnoses

Drag the “Diag 1” field into the new sheet

Next, drag the “Diabetes.csv (Count)” field

From the Show Me menu, select a Treemaps chart

To get the color of each square to show the proportion of patients readmitted before 30 days for the disease, drag “Readmitted <30” into Color, and set the Measure to Average.

Change the color to Custom sequential. For this, click on the black arrow next to the color legend and select the option Edit Colors. Then select “Custom Sequential” from the dropdown menu. Feel free to experiment with different colors, or leave it as is.

Drag the field “Disease Name” from the disease_categories.csv table into Label. This way, you can get the name of the diagnostic, rather than just the code.

You should get a chart that looks something like this:


## Exercise 12: Tables
Lastly, you want to analyze how readmission patterns vary across medical specialties and age groups to identify specific provider-patient combinations that may benefit from enhanced discharge planning protocols.

Create a new sheet called “Medical Specialty”

Drag the field “Medical Speciality” into Rows

Drag “Readmitted” into Columns

Drag “Age” also into Rows

Drag “diabetes.csv (Count)” into Label. This is the value you will complete the table with

Filter out missing values in the Medical Specialty field, which are represented with the question mark character “?”

Customize the table 

Drag “diabetes.csv (Count)” into Color

For the color, add a Quick Table Calculation and select Percent of Total

Change how the table calculation is made by going to Compute Using and select “Pane”. This will compute the percentage per block in the table

Change the color scale to Green-Blue diverging

Change the title of the color scale legend to “% of Patients per Medical Specialty”

Add the rows grand total by clicking in the Analysis menu, then going to Totals, and selecting Show Row Grand Totals



