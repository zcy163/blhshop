# blhshop
## Python 3.9.6 + Django + RestFramework

### project run

cd [project_name]
virtualenv nenv
source nenv/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver

### tests

http://127.0.0.1:8000/rest/1.0/tests/v1/index

### admin

http://127.0.0.1:8000/admin/
admin
Bai@2022

## Git

### 1、切换到自己的分支进行开发

git checkout [-b, -B] [自己的分支]  // [-b, -B]是创建分支，如果已存在该分支不需要这个参数

### 2、提交代码前先更新dev分支代码

git checkout [-b, -B] dev  // [-b, -B]是创建分支，如果已存在该分支不需要这个参数
git pull origin dev

### 3、回到自己的分支合并代码

git checkout [自己的分支]
git add [需要提交的文件]
git commit -m '[修改内容描述]'
git stash  // 备份当前工作区，防止跟不需要提交的代码冲突
git rebase dev  // 合并dev

### 4、提交代码到dev

git push origin refs/heads/dev
git stash pop  // 恢复当前工作区，如果提交代码是备份了


"pages/home/home",
"pages/usercenter/index",
"pages/usercenter/person-info/index",
"pages/usercenter/address/list/index",
"pages/usercenter/address/edit/index",
"pages/goods/list/index",
"pages/goods/details/index",
"pages/goods/category/index",
"pages/goods/search/index",
"pages/goods/result/index",
"pages/cart/index",
"pages/order/order-confirm/index",
"pages/order/receipt/index",
"pages/order/pay-result/index",
"pages/order/order-list/index",
"pages/order/order-detail/index",
"pages/goods/comments/index",
"pages/order/apply-service/index",
"pages/order/after-service-list/index",
"pages/order/after-service-detail/index",
"pages/goods/comments/create/index",
"pages/coupon/coupon-list/index",
"pages/coupon/coupon-detail/index",
"pages/coupon/coupon-activity-goods/index",
"pages/promotion-detail/index",
"pages/order/fill-tracking-no/index",
"pages/order/delivery-detail/index",
"pages/order/invoice/index",
"pages/usercenter/name-edit/index"

python manage.py runserver_plus --cert-file wxamp.blhlm.com.crt --key-file wxamp.blhlm.com.key 0.0.0.0:443
