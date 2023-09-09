# Notes on the problem and solution

- There is no data provided to give examples of what would be good or bad matches (a training data set).
  - This rules out any algorithm that is based on machine learning.
  - If there was more amount of members, it might be worth trying to identify clusters, but there's not enough data to 
    attempt to cluster either.
- Each data point in the files only has 2 features, which look simple enough and seem to have similar wording.
- The similarity in wording could be used to compute how much the member's description and the job's description have
  in common.
- Looking at the examples more closely:
  - Joe's bio is "I'm a designer from London, UK", which has "London" as a match with the location of job #3, and
    also has "London" and "designer" as matches with both location and title of job #6.
    - I believe the match with #6 should be stronger.
  - Marta's bio is "I'm looking for an internship in London", which matches the title of job #1, and matches both the
    title and location of jobs #3 and #5.
    - I believe the match with #3 and #5 should be stronger than with #1.
  - Hassan's bio uses the word "design" which should be matched with its variation "designer".
    - Here we may be entering the territory of NLP, which I will stay away from because of the complexity, but it is an
      option that should be considered.
  - Grace's and Daisy's bios have a complex explanation that the algorithm needs to understand.
    - For Grace, "London" is in the text, but it shouldn't be used for matching because she wants to be outside of
      London.
    - For Daisy, "Edinburgh" is in the text, but it shouldn't be used for matching because she wants to relocate to
      London.


# Conclusions and requirements identified from these notes:

- The member's bio can be used to check for similarity with both the job title and location.
- When checking for matches between words in the jobs and the members, this should be done in a way that accounts for
  different variations of the same word.
- (optional) If I get the time, it would be interesting to see how it performs to add a pre-step before any matching
  in which we transform every data point into a variant where only the root of the words is used. Eg: "I'm looking
  for a job in marketing outside of London" => "I am look for a job in market out of London"
- Word context: specific combinations of words will need to be given more importance when matching, eg. "relocating to"


# Approach I will follow:

- As some matches as weaker than others, I will be using a scoring system.
  - There will be a series of checks performed between jobs and members.
  - For each one that checks, it will add weight to the match.
  - There will be checks that may need to substract weight instead of adding.
  - The code will pick the match with the highest weight.
  - It will be the most rudimentary things, without number scaling, or percentage based. Just adding 1 for each check
    should be enough, as I've chosen this approach mostly to keep count of how many things about a job make it a good
    or not-so-good match.
- I'm going to make a first attempt at looking at word context.
  - However, I know that no matter what I come up with, it will not be good without proper NLP.
  - For example, if the code identifies "outside to London" and gives jobs in London a negative weight, then it will be
    doing the opposite to what it should in these cases:
    - "I am currently working outside of London, but I would like to move back to the city."
    - "I am very flexible with commute times, but will not consider anything outside of London."


# Dumping ground for notes of things I'm leaving aside while writing the code:

- lower() should be done on load. It's inefficient to do it every time the function is called.
- Word extraction should be properly done. "split()" isn't the way.
- As I'm writing this code, I'm realising I haven't thought properly about the topic of location: 
  - A job's match in terms of career should be given much more weight than in terms of location (maybe 10x at least?).
    I'm leaving this decision out of the code because it's completely "a finger in the air", but I'd personally prefer
    a software engineering job in Glasgow than being a performer in Edinburgh.
  - I think the proper way to go about it would be to calculate the distance between the job's location and the member's
    (in the cases where it is available, as Hassan doesn't mention where he's based).
- During the final step of gluing the functions I've written, I'm noticing that the time complexity is O(n^2), which
  seem excessive. This could be improved by using a document-based search approach, which would remove the need to loop
  through all jobs.
  - The main code for all recommendations is O(n^2), but I don't think that's the most common use case for a recommender
    tool. For example, Joe will never request to see the recommendations made to Marta. So, in the use case of Joe
    checking out jobs recommended to him, this would be O(n).
  - If this was to be put in a production system, I'd strongly recommend to store similarity scores somewhere so that
    they don't have to be re-computed again every time. This would require computing similarities only for new jobs as
    they come into the system and for new members (I think this concept is called online training or something like
    that in machine learning).
- I've separated everything I could into unit-testable functions with the purpose of writing unit tests for each
  component. However, you requested that I don't spend any more than 2 hours, so I'm stopping here. I'd love to have
  added unit tests!