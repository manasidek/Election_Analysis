# Election_Analysis

## Overview of Election Audit 

## Purpose of this election audit analysis
- The purpose of the analysis is to help a Board of Elections Employee to provide the audit of a recent local congressional election to the election commission.

## Resources
- Data Source: [Election Results]()

## Election-Audit Results
### The Analysis of the Election Show that:
- The total number of votes casted in this congressional election in the precinct are **369,711**
- The number of votes for each county in the precinct are as follows:

**County Votes**

| County Name | Vote Percentage |  Votes  |
|-------------|-----------------|---------|
| Jefferson   |      10.5%      | 38,855  |
|  Denver     |      82.8%      | 306,055 |
| Arapahoe    |      6.7%       | 24,801  |

	
- The largest number of votes casted are in ***DENVER*** county.


- The number of votes each candidate received are as follows:

| 	Candidate Name     | Vote Percentage |  Votes  |
|--------------------------|-----------------|---------|
| Charles Casper Stockham  |      23.0%      | 85,213  |
| Diana DeGette            |      73.8%      | 272,892 |
| Raymon Anthony Doane     |      3.1%       | 11,606  |



- The **Winning candidate** is ***DIANA DEGETTE***
- The **Winning Vote Count** is **272,892**
- The **Winning Percentage** is **73.8%**


##Election-Audit Summary

The script can be used to obtain the above election results for any other election, as it reads candidate and county names dynamically from the data and aggregates the vote counts accordingly. There will be minor modifications required in case the data for the other elections is in a different file location or format compared to the current. 

These modifications are explained below:
- File Name and File Path: The file name and path in the code snippet below will need to be updated to reflect the file name and path of the new election that needs to be analyzed.
- Data Format: The current data has 'Ballot ID', 'County Name' and 'Candidate Name' in that order. If this differs in the data for the new election, the script will need to be modified.
