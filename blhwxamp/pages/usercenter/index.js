import { fetchUserCenter } from '../../services/usercenter/fetchUsercenter';
import Toast from 'tdesign-miniprogram/toast/index';

const menuData = [
  [
    {
      title: '收货地址',
      tit: '',
      url: '',
      type: 'address',
    },
    {
      title: '订单管理',
      tit: '',
      url: '',
      type: 'order',
    },
    // {
    //   title: '优惠券',
    //   tit: '',
    //   url: '',
    //   type: 'coupon',
    // },
    // {
    //   title: '积分',
    //   tit: '',
    //   url: '',
    //   type: 'point',
    // },
  ],
  [
    {
      title: '帮助中心',
      tit: '',
      url: '',
      type: 'help-center',
    },
    {
      title: '客服热线',
      tit: '',
      url: '',
      type: 'service',
      icon: 'service',
    },
  ],
];

const orderTagInfos = [
  {
    title: '待付款',
    iconName: 'wallet',
    orderNum: 0,
    tabType: 5,
    status: 1,
  },
  {
    title: '待发货',
    iconName: 'deliver',
    orderNum: 0,
    tabType: 10,
    status: 1,
  },
  {
    title: '待收货',
    iconName: 'package',
    orderNum: 0,
    tabType: 40,
    status: 1,
  },
  {
    title: '待评价',
    iconName: 'comment',
    orderNum: 0,
    tabType: 60,
    status: 1,
  },
  {
    title: '退款/售后',
    iconName: 'exchang',
    orderNum: 0,
    tabType: 0,
    status: 1,
  },
];

const getDefaultData = () => ({
  showMakePhone: false,
  userInfo: {
    avatarUrl: '',
    nickName: '正在登录...',
    phoneNumber: '',
  },
  menuData,
  orderTagInfos,
  customerServiceInfo: {},
  currAuthStep: 2,
  showKefu: true,
  versionNo: '1.0.4',
  token: wx.getStorageSync('token')
});

Page({
  data: getDefaultData(),

  onLoad() {
    this.getVersionInfo();
  },

  getUserProfile(e) {
    // 推荐使用 wx.getUserProfile 获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认
    // 开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    wx.getUserProfile({
      desc: '用于完善会员资料', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        const {nickName, avatarUrl} = res.userInfo;
        this.userLogin(nickName, avatarUrl);
      },
    })
  },

  userLogin(nickName, avatarUrl) {
    const _this = this;
    wx.login({
      success (res) {
        if (res.code) {
          // console.log(res.code, nickName, avatarUrl)
          //发起网络请求
          wx.request({
            method: 'POST',
            url: 'https://wxamp.blhlm.com/rest/1.0/wxamp/v1/jscode2session',
            data: {
              js_code: res.code,
              username: nickName,
              image: avatarUrl
            },
            success: (res) => {
              // console.log(res.data)
              if (res.data.code === 0) {
                wx.setStorageSync('token', res.data.data.token);
                _this.fetUseriInfoHandle();
              } else {
                Toast({
                  context: _this,
                  message: res.data.msg,
                });
              }
            }
          })
        } else {
          console.log('登录失败！' + res.errMsg)
        }
      }
    })
  },

  onShow() {
    this.getTabBar().init();
    this.init();
  },
  onPullDownRefresh() {
    this.init();
  },

  init() {
    this.fetUseriInfoHandle();
  },

  fetUseriInfoHandle() {
    const _this = this;
    const token = wx.getStorageSync('token');
    if (!token || token === '') {
      this.setData({
        currAuthStep: 1
      });
      return;
    }
    this.setData({token});
    wx.request({
      method: 'POST',
      url: 'https://wxamp.blhlm.com/rest/1.0/user/v1/token',
      data: {token},
      success: (res) => {
        // console.log(res.data)
        if (res.data.code === 0) {
          const userInfo = res.data.data;
          this.setData({
            userInfo: {
              avatarUrl: userInfo.image,
              nickName: userInfo.username
            },
            currAuthStep: 2
          }, () => {
            wx.stopPullDownRefresh();
          })
        } else {
          Toast({
            context: _this,
            message: res.data.msg,
          });
          this.setData({
            currAuthStep: 1
          }, () => {
            wx.setStorageSync('token', '');
          })
        }
      }
    })
  },

  onClickCell({ currentTarget }) {
    const { type } = currentTarget.dataset;

    switch (type) {
      case 'address': {
        const token = wx.getStorageSync('token');
        if (!token || token === '') {
          Toast({
            context: this,
            message: '未登录'
          })
          break;
        }
        wx.navigateTo({ url: '/pages/usercenter/address/list/index' });
        break;
      }
      case 'order': {
        wx.navigateTo({ url: '/pages/order/order-list/index' });
        break;
      }
      case 'service': {
        this.openMakePhone();
        break;
      }
      case 'help-center': {
        Toast({
          context: this,
          selector: '#t-toast',
          message: '你点击了帮助中心',
          icon: '',
          duration: 1000,
        });
        break;
      }
      case 'point': {
        Toast({
          context: this,
          selector: '#t-toast',
          message: '你点击了积分菜单',
          icon: '',
          duration: 1000,
        });
        break;
      }
      case 'coupon': {
        wx.navigateTo({ url: '/pages/coupon/coupon-list/index' });
        break;
      }
      default: {
        Toast({
          context: this,
          selector: '#t-toast',
          message: '未知跳转',
          icon: '',
          duration: 1000,
        });
        break;
      }
    }
  },

  jumpNav(e) {
    const status = e.detail.tabType;

    if (status === 0) {
      wx.navigateTo({ url: '/pages/order/after-service-list/index' });
    } else {
      wx.navigateTo({ url: `/pages/order/order-list/index?status=${status}` });
    }
  },

  jumpAllOrder() {
    wx.navigateTo({ url: '/pages/order/order-list/index' });
  },

  openMakePhone() {
    this.setData({ showMakePhone: true });
  },

  closeMakePhone() {
    this.setData({ showMakePhone: false });
  },

  call() {
    wx.makePhoneCall({
      phoneNumber: this.data.customerServiceInfo.servicePhone,
    });
  },

  gotoUserEditPage(e) {
    const token = wx.getStorageSync('token')
    if (!token || token === '') {
      this.getUserProfile(e)
    }
    const { currAuthStep } = this.data;
    if (currAuthStep === 2) {
      wx.navigateTo({ url: '/pages/usercenter/person-info/index' });
    }
  },

  getVersionInfo() {
    const versionInfo = wx.getAccountInfoSync();
    const { version, envVersion = __wxConfig } = versionInfo.miniProgram;
    // this.setData({
    //   versionNo: envVersion === 'release' ? version : envVersion,
    // });
  },
});
