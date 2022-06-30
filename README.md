# ElectionAnalysis
# Overview of Election Audit

The goal of this project was to help Tom who is a Colorado board of election employee. We are assisting him is provide a tabulated election result for a US congressional district in Colorado. Tom in turn will present the summary of total number of votes cast, number of candidates and the votes casted for these candidate as a count and percentage of total votes to the election commission. We are also to announce the winner of this election detailing the winning votes in counts and percentages. 
  Based on our primary task the election commission had further requested additional data for;
  1. Voter turnout in each county.
  2. Percentage of votes from each county out of the total count. 
  3. The county with the highest turnout.
The output of this analysis will be included in a text file that should be easy to read for audience of any background.

## Election-Audit Results:
### Total number of votes casted in the congressional election
  * This election saw a good voter turnout and a total of **369,711** votes were casted across three counties. 

### Summary of number of votes and the percentage of total votes for each county in the precinct
  * The result of the number of votes cast and percentage of total votes are as follows:
  ** Denver county: 82.8% (306,055)
  ** Jefferson county: 10.5% (38,855)
  ** Arapahoe county: 6.7% (24,801)



### Challenges

For both the analysis the only major challenge was my unfamiliarity with excel functions. For the first analysis generating pivot tables and charts was fairly straight forward. One issue that I face was when filtered using the newly created "Years" column. I would not see months and I had to use the "Date ended conversion" column instead as it breaks down into quaters and months.

For the second analysis, my only complain would be typing the Goals column. I am sure that one could write a script to fill in this column, especially if there were more entries in this column than the 12 listed.

## Result

### Theater Outcome Based on Launch Date

The two conclusions that can be drawn from this analysis are;
1. Months May-July are most favorable to start a crowdfunding project. The success to fail ratio for these three months are quite similar (65%+/-2) and eventhough May would look the better month June would be not a distant second choice.
2. Setting up a crowdfunding project should be avoided in the month of December as there's a equal chance that it may fail. 

### Outcome Based on Goals

The clear conclusion here is not to set a crowdfunding goal between $45,000-$49,999 as it has a 100% chance of failure. 

## Limitation

1. One limitation is that this data is not current and relies on information collected between 2010-2017. To get a more realistic picture data generate from 2015-current should be considered.
