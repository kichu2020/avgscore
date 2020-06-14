'''names = ['a','b','c']
maths =[10,20,30]
physics = [80, 80, 56.3]
chemistry =[60,20,30]

The top scorer in Math , physics and chemistry
The lowert scorer in Math , physics and chemistry
The top scorer by taking the average
The lowert scorer by taking the average

Print name and score '''


names = ['a','b','c','d','e']
maths =[90,88,80,70,85]
physics = [83,85,96,80,56.3]
chemistry =[90,98,78,84,98]

high_score = 0
high_scorer = ''
low_score = 100
low_scorer = ''


for index, score in enumerate(maths):
  if score > high_score:
    high_score = score
    high_scorer = names[index]
  if score < low_score:
    low_score = score
    low_scorer = names[index]



print(f'The highest scorer is {high_scorer} and the mark is  {high_score}')
print(f'The loweest scorer is {low_scorer} and the mark is  {low_score}')
high_score = 0
high_scorer = ''
low_score = 100
low_scorer = ''

for index, score in enumerate(physics):
  if score > high_score:
    high_score = score
    high_scorer = names[index]
  if score < low_score:
    low_score = score
    low_scorer = names[index]



print(f'The highest scorer is {high_scorer} and the mark is  {high_score}')
print(f'The loweest scorer is {low_scorer} and the mark is  {low_score}')


high_score = 0
high_scorer = ''
low_score = 100
low_scorer = ''

for index, score in enumerate(chemistry):
  if score > high_score:
    high_score = score
    high_scorer = names[index]
  if score < low_score:
    low_score = score
    low_scorer = names[index]



print(f'The highest scorer is {high_scorer} and the mark is  {high_score}')
print(f'The loweest scorer is {low_scorer} and the mark is  {low_score}')



high_score = 0
high_scorer = ''
low_score = 100
low_scorer = ''

for index, name in enumerate(names):
  avg_score=(maths[index]+physics[index]+chemistry[index])/3
  if avg_score > high_score:
    high_score = avg_score
    high_scorer = names[index]
  if avg_score < low_score:
    low_score = avg_score
    low_scorer = names[index]



print(f'The highest average scorer is {high_scorer} and the mark is  {high_score}')
print(f'The loweest average scorer is {low_scorer} and the mark is  {low_score}')
