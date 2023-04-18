import { fetchHome } from '../../services/home/home';
import { fetchGoodsList } from '../../services/good/fetchGoods';
import { dispatchCommitPay } from '../../services/order/orderConfirm';
import Toast from 'tdesign-miniprogram/toast/index';

Page({
  data: {
    addressVisible: false,
    searchValue: '',
    searchList: [],
    searchVisible: false,
    visible: false,
    nomore: false,
    tabIndex: 0,
    imgSrcs: [],
    tabList: [],
    goodsList: [],
    goodsListLoadStatus: 0,
    pageLoading: false,
    current: 1,
    autoplay: true,
    duration: 500,
    interval: 5000,
    navigation: { type: 'dots' },
    filters: '',
    screenIndex: 0,
    selectGoodsId: '',
    screenMenu: [
      {
        name: '最近更新',
        active: 0,
        key: 'item_apply_time',
        visible: false,
        value: '',
        categorys: [
          { label: '5', value: '5' },
          { label: '2', value: '2' },
        ],
      },
      {
        name: '销量',
        active: 0,
        key: 'item_volume',
        visible: false,
        value: '',
        categorys: [
          { label: '3', value: '3' },
          { label: '2', value: '2' },
        ],
      },
      {
        name: '库存',
        active: 0,
        key: 'item_stock',
        visible: false,
        value: '',
        categorys: [
          { label: '2', value: '2' },
          { label: '2', value: '2' },
        ],
      },
      {
        name: '到手价',
        active: 0,
        key: 'item_price',
        visible: false,
        value: '',
        categorys: [
          { label: '7', value: '7' },
          { label: '2', value: '2' },
        ],
      },
    ],
    pickerTitle: '',
  },

  goodListPagination: {
    index: 1,
    num: 10,
  },

  privateData: {
    tabIndex: 0,
  },

  onShow() {
    this.getTabBar().init();
  },

  onLoad(option) {
    if (option && option.searchValue) {
      this.setData({
        searchValue: option.searchValue
      }, () => {
        this.init();
      })
    } else {
      this.init();
    }
  },

  onReachBottom() {
    if (this.data.goodsListLoadStatus === 0) {
      this.loadGoodsList();
    }
  },

  onPullDownRefresh() {
    this.init();
  },

  init() {
    this.loadHomePage();
    this.setSearchList();
  },

  setSearchList() {
    let searchList = wx.getStorageSync('search')
    if (searchList && searchList.length > 10) {
      searchList = searchList.slice(0, 10)
    }
    this.setData({searchList})
  },

  loadHomePage() {
    wx.stopPullDownRefresh();

    this.setData({
      pageLoading: true,
    });
    fetchHome().then(({ swiper, tabList }) => {
      this.setData({
        tabList,
        imgSrcs: swiper,
        pageLoading: false,
      });
      this.loadGoodsList(true);
    });
  },

  tabChangeHandle(e) {
    // this.privateData.tabIndex = e.detail;
    // console.log(e);

    const filters = e.detail.label
      ? e.detail.label
      : e.currentTarget.dataset.label;
    const tabIndex = isNaN(e.detail.value)
      ? e.currentTarget.dataset.value
      : e.detail.value;

    // console.log(filters, tabIndex);
    this.setData(
      {
        filters: tabIndex === 0 ? '' : filters,
        tabIndex,
        visible: false,
      },
      () => {
        this.loadGoodsList(true);
      },
    );
  },

  onReTry() {
    this.loadGoodsList();
  },

  tabsDown() {
    this.setData({
      visible: !this.data.visible,
    });
  },

  async loadGoodsList(fresh = false) {
    if (fresh) {
      wx.pageScrollTo({
        scrollTop: 0,
      });
    }

    this.setData({ goodsListLoadStatus: 1 });

    const { screenMenu } = this.data;
    const { screenIndex } = this.data;
    const pageSize = this.goodListPagination ? this.goodListPagination.num : 4;

    const sort = screenMenu[screenIndex].key;
    const { filters } = this.data;

    let pageIndex = 0;
    if (this.privateData && this.goodListPagination) {
      pageIndex = this.privateData.tabIndex * pageSize + this.goodListPagination.index + 1;
    }

    if (fresh) {
      pageIndex = 1;
    }

    pageIndex = pageIndex > 0 ? pageIndex : 1;

    const options = {
      sort,
      filters,
      search: this.data.searchValue
    };
    // console.log(pageIndex)

    try {
      const nextList = await fetchGoodsList(pageIndex, pageSize, options);
      // console.log(nextList)
      this.setData({
        goodsList: fresh ? nextList : this.data.goodsList.concat(nextList),
        goodsListLoadStatus: 0,
        nomore: false
      });

      if (nextList.length === 0) {
        Toast({
          context: this,
          message: '未搜索到更多商品',
        });
        this.setData({
          nomore: true
        })
      }

      this.goodListPagination.index = pageIndex;
      this.goodListPagination.num = pageSize;
    } catch (err) {
      this.setData({ goodsListLoadStatus: 3 });
    }
  },

  goodListClickHandle(e) {
    const { index } = e.detail;
    const { spuId } = this.data.goodsList[index];
    wx.navigateTo({
      url: `/pages/goods/details/index?spuId=${spuId}`,
    });
  },

  goodListAddCartHandle(e) {
    const token = wx.getStorageSync('token');
    if (!token || token === '') {
      Toast({ context: this, message: '未登录'});
      return;
    }
    const { spuId } = e.detail.goods;
    this.setData({
      selectGoodsId: spuId,
      addressVisible: true
    })
  },

  selectAddressHandle(e) {
    const _this = this;
    const { addressId } = e.detail;
    const goodsId = this.data.selectGoodsId;
    const token = wx.getStorageSync('token');
    // console.log(token, goodsId, addressId)
    dispatchCommitPay({
      token,
      goods: goodsId,
      address: addressId
    }).then((res) => {
      if (res.code === 0) {
        Toast({ context: _this, message: '已提交'});
      } else {
        Toast({ context: _this, message: res.msg});
      }
    }).catch(() => {
      Toast({ context: _this, message: '提交失败'});
    })
  },

  navToSearchPage() {
    wx.navigateTo({ url: '/pages/goods/search/index' });
  },

  handleBlur() {
    this.setData({
      searchVisible: false
    })
  },

  handleFocus() {
    this.setSearchList();
    this.setData({
      searchVisible: true,
    })
  },

  handleClear() {
    this.setData({
      searchValue: '',
    }, () => {
      this.loadGoodsList(true);
    })
  },

  handleSearch(e) {
    // console.log(e.target.dataset.value)
    this.setData({
      searchValue: e.target.dataset.value
    }, () => {
      this.loadGoodsList(true);
    })
  },

  handleSubmit(e) {
    const searchValue = e.detail.value;
    const search = wx.getStorageSync('search');
    if (search) {
      if (search.indexOf(searchValue) === -1) {
        search.unshift(searchValue)
        wx.setStorageSync('search', search)
      }
    } else {
      wx.setStorageSync('search', [searchValue])
    }
    this.setData({searchValue}, () => {
      this.loadGoodsList(true);
    })
  },

  navToActivityDetail({ detail }) {
    const { index: promotionID = 0 } = detail || {};
    wx.navigateTo({
      url: `/pages/promotion-detail/index?promotion_id=${promotionID}`,
    });
  },

  onClickPicker(e) {
    // const { key, index } = e?.currentTarget?.dataset;
    const index = e?.currentTarget?.dataset.index;
    // const { screenMenu } = this.data;
    // console.log(screenMenu[index].key)
    this.setData(
      {
        screenIndex: index,
      },
      () => {
        this.loadGoodsList(true);
      },
    );
    // screenMenu[index].visible = true;
    // this.setData({ screenMenu });
  },

  onPickerChange(e) {
    // const { key, index } = e?.currentTarget?.dataset;
    const index = e?.currentTarget?.dataset.index;
    const { screenMenu } = this.data;
    screenMenu[index].value = e.detail.label[0];
    screenMenu[index].visible = false;
    this.setData({ screenMenu });
    this.loadGoodsList(true);
  },

  onPickerCancel(e) {
    // const { key, index } = e?.currentTarget?.dataset;
    const index = e?.currentTarget?.dataset.index;
    const { screenMenu } = this.data;
    screenMenu[index].visible = false;
    this.setData({ screenMenu });
  },

  onShareAppMessage() {
    return {};
  },
});
