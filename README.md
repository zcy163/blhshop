# blhshop
Python 3.9.6 + Django + RestFramework
project run
cd [project_name] virtualenv nenv source nenv/bin/activate python -m pip install -r requirements.txt python manage.py runserver

tests
http://127.0.0.1:8000/rest/1.0/tests/v1/index

admin
http://127.0.0.1:8000/admin/

Git
1、切换到自己的分支进行开发
git checkout [-b, -B] [自己的分支] // [-b, -B]是创建分支，如果已存在该分支不需要这个参数

2、提交代码前先更新dev分支代码
git checkout [-b, -B] dev // [-b, -B]是创建分支，如果已存在该分支不需要这个参数 git pull origin dev

3、回到自己的分支合并代码
git checkout [自己的分支] git add [需要提交的文件] git commit -m '[修改内容描述]' git stash // 备份当前工作区，防止跟不需要提交的代码冲突 git rebase dev // 合并dev

4、提交代码到dev
git push origin HEAD:refs/heads/dev git stash pop // 恢复当前工作区，如果提交代码是备份了
