print('back to main branch and going to commit 6')

print('faltu ka commit 7')

print('learned the concept of branching and merging',
      'accidentally did non-fast-forward merge',
      'it was intresting. basically in main 1, 2 3,6 and 7 commits are there',
      'in helper branch at 3rd commit, 4 and 5 commits are there.' \
      'I merge helper to mail and it create like below')


'original structure'
'main branch    : 1---2---3---6---7'
'helper branch  :         \__ 4---5'

'After merge it lloks like below'
'''
*   e7b407a (HEAD -> main) Merge helper_branch into main
|\  
| * 47883db commit 5: one more commit in helper branch
| * 4f13600 commit 4: helper branch created
* | f9245f2 commit 7 -  faltu commit
* | 0e1a51d commit 6 - back to main branch
|/  
* c7f76e8 third commit- credentials moved to .gitignore
* fa2c985 second commit - created credentials file
* 789ffba first commit
'''


'hi lets try avoiding merge conflicts'

'HI adding something in detach branch'
