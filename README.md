# Gilmore_Girls_Episode_Writer

In an effort to generate new episodes of a favorite show of mine, I thought why not use machines and let them work for my entertainment.

The data was scraped from ... and saved to a text file. 
For a first approach I used a neural network of the long short-time memory (LSTM) type, due to their favourable characteristics for word processing and NLP. To fit the model found in "gg_generator_lstm.py", the time per epoch was about 2.5 hours. For a first approximation the epoch number was set to 4, reducing the loss to 1.91. After the fitting, the model printed some very underwhelming dialogue of:
> "lorelai ok go sory lorelai ok go sory lorelai ok go sory lorelai ok go sory lorelai ok go sory lorelai ok go sory lorelai" 

Well at least, running the code in Goole Colab Notebooks sped the computation up enormously, reducing the computation time per epoch to about 2 minutes. After another 4 epochs of fitting the model the loss was further reduced to 1.73, albeit the resulting dialogue still doesn't seem very promising:
> "l lorelai oh go lorelai oh go lorelai oh go lorelai oh go"

This made me look for alternate ways to tackle the problem, and I've come across a way to predict text sequences on character basis by a maximum-likelihood algorithm. The corresponding code can be found in the file "Max_Likelihood_GG_Generator.py" Trainig this on the dialogue of the first season of Gilmore Girls leads to the following generated text:
> 'written by Daniel Palladino directed by Michael Katleman transcrpt by Vanessa LORELAI Oh dear God Almighty That is what you thought the medallion and want the blossoms JACKSON Sookie SOOKIE I need some entertainment RORY No I do not either MAX That is for me MADELINE Looks like she just fell off the roof Sookie is chocolate cake a lamp chopmashed potatoes RORY From a box DEAN But they were nothing to do with myself now You live to take her EMILY Well I am gonna go check up on Rachel LORELAI Well you know I was really angry about it in the fridge I am not sure that carpet is replaced that all about school What are you talking about EMILY Well your grandparents on Friday Maybe we could sit together and he did LORELAI So God is a woman RICHARD Lorelai I just tried some of Mom too LORELAI What EMILY I mean tonight LORELAI I will pick you up the story of how Stars Hollow High LANE You ca not RORY Thank you DEAN Right outside cultural influence especially the rose garden RICHARD Emily EMILY '

Now this actually looks more like it.
