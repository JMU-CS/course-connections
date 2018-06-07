# Course Connections Visualization

The graph-data.txt should contain a list of courses and their topic tags. A course is given by a line containing the course number followed by the course title, such as

CS 149 Intro to Programming

and then one or more topic tags, each on its own line beginning with a hashtag, like

#programming
#logic

etc. Finally, a blank line is used to separate courses. 

To update the graph, run the gen_chord_graph.py tool, which will output a JavaScript snippet to be pasted into the chord_diagram.htm page. Obviously this should be streamlined, but this is future work. 


# Wishlist

* Would like to have topics highlight in some pleasing way when a user mouses over a course. 
* Would like to click on a topic and view all courses with the topic. 
* Is there a better color scheme for all this? I don't know. 
* What is readme.json? I don't know. Maybe it should be deleted? Maybe it is necessary? I forgot, but I'm not looking into it now, so here you go GitHub!
