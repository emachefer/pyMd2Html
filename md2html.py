#!/usr/bin/python3
#########################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>
#########################################
# Description: This program transform a markdow file
# to a HTML file.
#########################################
# Author: Evan Machefer
# Date:   2020
# Email:  evan.machefer@gmail.com
#########################################

# IMPORTS
import sys
import re

# Get raw md file
def getMd(infile):
    mdString = list()
    with open(infile, 'r') as ifile:
        for line in ifile:
            mdString.append(line)
    return mdString

# Transform markdown symbols to HTML tags
def getHtml(mdString):
    inString = ""
    for line in mdString:
        # print(line)
        if line[0] == "#":
            if line[1] == "#":
                inString += line.replace("##" , "<h2>")+"</h2>"
            else:
                inString += line.replace("#", "<h1>")+"</h1>"
        elif line[0] == "*":
            inString += line.replace("*","<li>")+"</li>"
        else:
            inString += line
    return inString

# Define a HTML wrapper
def htmlWrap(inString, title=""):
    css = "h1, h2, h3, h4{text-align:center;}"# TODO : custom css file
    head = "<html><head><title>"+title+"</title><style>"+css+"</style></head><body>"
    lastString = "</body></html>"
    return str(head + str(inString) +lastString)

# Define help
def help():
    return "\n\tThis program transform a markdown file to a HTML file\n\n\
Usage: md2html <INFILE.md> <OUTFILE.html>\n\
Help: md2html -h OR md2html --help"


# Main function
if __name__=="__main__":
    try:
        inFile = sys.argv[1]
        outFile = sys.argv[2]
    except:
        print(help())
        # tb = sys.exc_info()[2]
        # raise Exception.with_traceback(tb)
    else:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(help())
        else:
            mdString = getMd(inFile)
            inString = getHtml(mdString)
            with open(outFile, 'w') as ofile:
                ofile.write(htmlWrap(inString, "A savoir"))
