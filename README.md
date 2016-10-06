# Clinvitae Clone

## Assignment

Create a genomic variant web application that allows a user to search for
genomic variants based on a gene name and display the results in a tabular
view.

## Features

1. A user will enter a gene name and hit a search button which will result in a
   list of genomic variants for that gene being displayed.  The display of the
list of genomic variants will be in a tabular view that allows the user to see
the various attributes associated with each genomic variant.

2. To assist the user with entering the gene name to search for, provide a
   type-ahead or auto-suggest feature such that upon typing the first two or
more letters of a gene name, a list of gene names that start with those
characters is available for the user to choose from.

3. Provide two RESTful endpoints supporting the functionality listed in steps 1
   and 2 so that it can be easily consumed by other applications such as
command-line apps or reused by the genomic variant web application itself if it
is implemented as a single-page app.

## Datasource

A zipped TSV file containing over 120K variants is available at
http://clinvitae.invitae.com/download which should serve as the list of genomic
variants that the web application would search on.  Each row in the TSV file
represents a genomic variant and contains a gene column that represents the
gene name that this variant is associated with.  A genomic variant will have
one and only one gene name that it belongs to, but multiple genomic variants
can belong to the same gene name.

## Implementation

Feel free to use any application server, web framework, programming languages,
database technologies, third-party libraries, etc. that you think would be
appropriate to build the genomic variant web application.

Our expectation is that you will be writing some server code, client code, and
applying some basic styling to display the results in a functional web
application.  The goal is to have a working app that spans the full stack
instead of coming up with a design-winning UI that is beautiful but not
functional.  With that said, feel free to be creative in any aspect of the
application that you feel like would reveal your strengths or interests to us
as your time permits.

We understand that your time is precious so we are not expecting this
assignment to take more than 2-3 hours.

A more, full-featured version of a genomic variant web application that we have
developed here at Invitae can be found at http://clinvitae.invitae.com.  It is
NOT meant for you to copy or implement all of the features available in
Clinvitae, but rather you can use it to get more clarity and as an example of
how the web application should behave.  We are more interested in finding out
how you would build a working prototype of this web application than to have
you come up with a clone of Clinvitae.

## Submitting Your Solution

Please provide a zip file with your solution along with some instructions on
how to run your application in a simple README file.  If you would like to post
your solution on bitbucket or github instead and share the repo with us, that
would be fine as well.

## Questions and Feeback

Please feel free to email us if any part of the assignment is unclear.  We will
do our best to respond to your email questions as soon as possible.
