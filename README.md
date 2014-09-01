# About `mini_qa`

`mini_qa` is a toy question-answering program originally written by [Michael Nielsen](http://michaelnielsen.org/).  It uses Google to attempt to answer questions of the form "Who... ?".

An example question is: "Who discovered relativity?"

The design is inspired by the AskMSR system developed by researchers
at Microsoft Research.  The original paper is:

Brill, Lin, Banko, Dumais and Ng, "Data-Intensive Question
Answering" (2001).

The original author of this program, Michael Nielsen, described background to this program
[here](http://www.michaelnielsen.org/ddi/how-to-answer-a-question-a-simple-system/)
and
[here](http://www.michaelnielsen.org/ddi/using-evaluation-to-improve-our-question-answering-system/).

The present fork of `mini_qa` was created by [Marco Kuhlmann](http://www.ida.liu.se/~marku61/) for use in a course at [Linköping University](http://www.liu.se/) called [Perspectives on information technology](https://www.ida.liu.se/~TDDD39/).

# Installation and useage

Clone the repository and run the script:

	% python mini_qa.py

(This assumes that `python` points to Python 3.)

# Copyright and licensing

MIT License

Except the files `google.py` all files in this
repository are copyright (c) 2012 Michael Nielsen

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
