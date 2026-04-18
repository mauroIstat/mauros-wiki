# Neural Networks Unveiled:

- Source file: `raw/teaching/2026-slides-neural-networks-unveiled.pdf`
- Document type: `teaching`

## Extracted Text

Neural Networks Unveiled:
From Perceptrons to Transformers (The Moments
That Shaped Modern AI)
Mauro Bruno
University of Bergamo, Arpil 17, 2026

Who is shaping the future of AI?
In 2025, TIME namedthe architects of
AIas“Person of the Year” .
These are the people shaping the
technologies you are using to study, code,
generate images, or even ask for help
with your homework.
Have you ever heard of them?

Let’s start with a quick test
I’d like to understand how familiar you
are with AI.
Take your phone and scan the QR code.
Try to answer a few quick questions
No grades at the end, I promise :)

Neural Networks Unveiled
▶Why Learning Is Hard for Machines
▶Computer Vision
▶Language Models
▶Vibe Coding

The Human Visual System
The human visual system is one of
the greatest wonders we know.
With only20 wattsof power, our brain
can instantly recognize objects, faces,
and handwritten digits.
This ability emerges frombillions of
interconnected neurons.
Can we teach machines do the same?

A simple test for machine intelligence
Look at these handwritten digits.
Can you read them instantly? Of course you can.
But how would a machine do this?
For machines, this task is surprisingly hard.

Let’s try to write a program
Too much variability for fixed rules.
The real world is messy.

What if machines could learn the rules?
Instead of writing the rules, we let the machinelearn from examples.

Learning useful representations
Learning is not only about finding the correct
output.
A good model must build aninternal
representationof the data that makes the final
decision simpler.
Sometimes, the problem is not the data itself,
but the way the data is represented.
Can we separate these two classes with a
simple rule?

What if we change the representation?
A difficult problem can become
much simpler in adifferent
representation space.
The data points do not change,
only the way we represent them.
This is one of the key ideas
behind machine learning:
Learning useful representations that make decisions easier.

The Artificial Neuron
Inputs→Weights→Sum→Activation→Output
This is our building block

Learning the weights
How does learning work?
•The model makes a prediction
•We compare it with the correct answer
•If it’s wrong→we adjust the weights
•We try again
Learning≈updating the weights
This simple idea, was implemented in one of the first learning machines.

The first learning machine
1957 - Frank Rosenblatt
First implementation of a learning
algorithm
TheMark I Perceptron:
•A physical implementation
•Learns from examples
•Inspired by the human brain
The idea was wonderful, but results were limited
It took decades to make real progress

Neural Networks Unveiled
▶Why Learning Is Hard for Machines
▶Computer Vision
▶Language Models
▶Vibe Coding

Can machines see?
Let’s get back tohandwritten digitrecognition
We’ve seen that this is easy for humans. . .
But surprisingly hard for machines.
So. . . how do we solve this?
Let’s begin our journey into computer vision

What is an image?
An image is just a matrix of pixels
Each pixel has a value
For a machine. . . it’s just numbers.

1994 – MNIST Dataset
The MNIST dataset (Modified National
Institute of Standards and Technology) is
a foundational dataset in machine
learning:
•70,000 images (28×28 pixels)
•Each image is labeled (0–9)
•Format: Grayscale (8-bit, 0-255).
•Standard benchmark for machine
learning
A simple dataset. . . that changed everything

How do we use this data?
784 inputs→Neural Network→10 outputs

What’s the problem?
A fully connected networktreats every pixel independently
•Too many parameters to learn (∼110k)
•No notion ofspatial structure
•Nearby pixels are not treated as related
•Everything is connected to everything
We are ignoring the spatial structure of images

Detecting edges in an image
We can apply a simplefilter,
that detects changes in intensity.
This filter highlights the
edges.
What if the model could learn these filters?

Learning features
Neural networks learnhierarchical features
From simple patterns to complex representations
From edges→to parts→to objects

Convolutional Neural Networks
From pixels→to shapes→to digits

LeCun & LeNet
LeNet -— one of the first Convolutional Neural
Networks
•Developed at AT&T Bell Laboratories in the
1990s
•Designed for handwritten digit recognition
•Used in real-world applications (e.g. bank
check reading)
▶LeNet in action (YouTube)
But then. . . progress slowed down

2009 – Imagenet
ImageNet was not just a dataset.
It changed the scale of AI.
•14+ millionimages
•20,000+categories
•Millions of human annotations
Fei-Fei Li led ImageNet —- you may
remember her from the TIME cover
And progress started again.

ILSVRC – The Hardest Vision Challenge
Benchmarks used to be simple:
•Dog
•Cat
•Bird
ILSVRC changed the game.
Not just “dog”→
but 120 different dog breeds.
And every year, teams competed to win.

2012 – AlexNet
For years, traditional methods
struggled with ImageNet.
Then, in 2012, adeep neural
networkentered the
competition.
The error rate dropped
dramatically.
Deep learning worked.

The end of AI winter
For decades,Geoffrey Hintonbelieved
in neural networks.
Most of the field did not.
In 2012, AlexNet proved them
wrong.
It wasn’t just a better model.
It was the beginning of the AI revolution

Neural Networks Unveiled
▶Why Learning Is Hard for Machines
▶Computer Vision
▶Language Models
▶Vibe Coding

From Images to Language
We trained machines to recognize images. But can a machine describe what it sees?
From pixels→to words

Can You Guess the Next Word?
Let’s consider the following example:
”Artificial Intelligence is shaping the . ”
Possible predictions:
•world
•economy
•future
•society
A language model assigns probabilities and picks the most likely word.

How a Language Model works
From text→to probabilities→to words

Why This Naive Approach Fails?
Looks good, but...
•Neural Networks process
numbers, not words.
•We need toconvert words into
tokens and vectors.
This is the role ofTokenizationandEmbeddingsin Language Models.

Tokenization: Breaking Text into Pieces
What is Tokenization?
Splits text into smaller units calledtokens.
•Words(e.g.,"Artificial")
•Subwords(e.g.,"Intelli","gence")
•Characters(e.g.,"A","r", ...)
The tokenizer builds avocabulary of sizeN,
assigning a unique integer to each token.

Embeddings: From Tokens to Vectors
What are Embeddings?
•Neural Networks work withvectors of
numbers, not identifiers.
•Anembedding layerconverts each
token identifier into adense vectorof
fixed size.
•These vectors capturesemantic
relationshipsbetween tokens.
Let’s delve into embedding spaces...

Embeddings: Capturing Meaning in Vectors
•Word Embeddingsmap words todense vectorsin a continuous space.
•Thedistancebetween vectors reflectssemantic similaritybetween the
corresponding words.
•These vectors capturerelationshipsbetween different words.
•Traditional word embeddings providea single vector representationfor
each word, regardless of context.
•Directions in this space encodesemantic dimensions, such as: gender,
plurality and verb tense.
Embeddings allow neural networks to generalize and understand relationships
between words.

Visualizing Word Embeddings
Words in a Vector Space
The simplest way to grasp the intuition behind word embeddings is to visualize
how words are placed in avector space.

Can You Guess the Next Word?
We add an Embeddings layer:
•Input words are mapped todense
numerical vectors.
•The Neural Network processes these
vector representations.
•The output vectors are then
decoded back into words.

Meaning depends on context
•Same word, different meanings
•Context determines meaning
So. . . how do machines understand context?

2017 – Attention is all you need
In 2017, a new architecture changed
language modeling.
Instead of processing words one by one,
the Transformer looks at the whole
sentence and learns which words matter
most.
This idea is calledattention.
The model can focus on the words
that matter.

Neural Networks Unveiled
▶Why Learning Is Hard for Machines
▶Computer Vision
▶Language Models
▶Vibe Coding

Vibe Coding
A new way of coding?
•Less typing, more prompting
•Less control, more intuition
•Code is generated, not written
”It’s not really coding anymore...
it just mostly works. ”
Would you trust code you didn’t
write?

From Coding to Vibe Coding

Q&A
Thank you for listening!
Feel free to contact me:
mbruno@istat.it
