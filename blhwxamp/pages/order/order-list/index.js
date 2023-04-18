import { OrderStatus } from '../config';
import {
  fetchOrders,
  fetchOrdersCount,
} from '../../../services/order/orderList';
import { cosThumb } from '../../../utils/util';

Page({
  page: {
    size: 10,
    num: 1,
  },

  data: {
    tabs: [
      { key: -1, text: '全部' },
      { key: OrderStatus.PENDING_PAYMENT, text: '待付款', info: '' },
      { key: OrderStatus.PENDING_DELIVERY, text: '待发货', info: '' },
      { key: OrderStatus.PENDING_RECEIPT, text: '待收货', info: '' },
      { key: OrderStatus.COMPLETE, text: '已完成', info: '' },
    ],
    curTab: -1,
    orderList: [],
    listLoading: 0,
    pullDownRefreshing: false,
    emptyImg:
      'https://cdn-we-retail.ym.tencent.com/miniapp/order/empty-order-list.png',
    backRefresh: false,
    status: -1,
  },

  onLoad(query) {
    let status = parseInt(query.status);
    status = this.data.tabs.map((t) => t.key).includes(status) ? status : -1;
    this.init(status);
    this.pullDownRefresh = this.selectComponent('#wr-pull-down-refresh');
  },

  onShow() {
    if (!this.data.backRefresh) return;
    this.onRefresh();
    this.setData({ backRefresh: false });
  },

  onReachBottom() {
    if (this.data.listLoading === 0) {
      this.getOrderList(this.data.curTab);
    }
  },

  onPageScroll(e) {
    this.pullDownRefresh && this.pullDownRefresh.onPageScroll(e);
  },

  onPullDownRefresh_(e) {
    const { callback } = e.detail;
    this.setData({ pullDownRefreshing: true });
    this.refreshList(this.data.curTab)
      .then(() => {
        this.setData({ pullDownRefreshing: false });
        callback && callback();
      })
      .catch((err) => {
        this.setData({ pullDownRefreshing: false });
        Promise.reject(err);
      });
  },

  init(status) {
    status = status !== undefined ? status : this.data.curTab;
    this.setData({
      status,
    });
    this.refreshList(status);
  },

  getOrderList(statusCode = -1, reset = false) {
    const params = {
      parameter: {
        pageSize: this.page.size,
        pageNum: this.page.num,
      },
    };
    console.log(params)
    if (params.parameter.pageNum === 0) {
      params.parameter.pageNum = 1;
    }
    if (statusCode !== -1) params.parameter.orderStatus = statusCode;
    this.setData({ listLoading: 1 });
    return fetchOrders(params)
      .then((res) => {
        this.page.num++;
        let orderList = [];
        if (res && res.list) {
          orderList = (res.list || []).map((order) => {
            return {
              id: order.id,
              orderNo: order.uid,
              // parentOrderNo: order.parentOrderNo,
              // storeId: order.storeId,
              // storeName: order.storeName,
              status: order.status,
              // statusDesc: order.orderStatusName,
              // amount: order.paymentAmount,
              // totalAmount: order.totalAmount,
              // logisticsNo: order.logisticsVO.logisticsNo,
              createTime: order.create_time,
              goodsList: (order.goodsInfo || []).map((goods) => ({
                id: goods.item_id,
                thumb: cosThumb(goods.item_img_url, 70),
                title: goods.item_title,
                // skuId: goods.skuId,
                // spuId: goods.spuId,
                // specs: (goods.specifications || []).map(
                //   (spec) => spec.specValue,
                // ),
                price: goods.item_price,
                // num: goods.buyQuantity,
                // titlePrefixTags: goods.tagText ? [{ text: goods.tagText }] : [],
              })),
              buttons: order.buttonVOs || [],
              groupInfoVo: order.groupInfoVo,
              freightFee: order.freightFee,
            };
          });
        }
        // console.log(orderList)
        return new Promise((resolve) => {
          if (reset) {
            this.setData({ orderList: [] }, () => resolve());
          } else resolve();
        }).then(() => {
          this.setData({
            orderList: this.data.orderList.concat(orderList),
            listLoading: orderList.length > 0 ? 0 : 2,
          });
        });
      })
      .catch((err) => {
        this.setData({ listLoading: 3 });
        return Promise.reject(err);
      });
  },

  onReTryLoad() {
    this.getOrderList(this.data.curTab);
  },

  onTabChange(e) {
    const { value } = e.detail;
    this.setData({
      status: value,
    });
    this.refreshList(value);
  },

  getOrdersCount() {
    return fetchOrdersCount().then((res) => {
      const tabsCount = res.data || [];
      const { tabs } = this.data;
      tabs.forEach((tab) => {
        const tabCount = tabsCount.find((c) => c.tabType === tab.key);
        if (tabCount) {
          tab.info = tabCount.orderNum;
        }
      });
      this.setData({ tabs });
    });
  },

  refreshList(status = -1) {
    this.page = {
      size: this.page.size,
      num: 1,
    };
    this.setData({ curTab: status, orderList: [] });

    return Promise.all([
      this.getOrderList(status, true),
      this.getOrdersCount(),
    ]);
  },

  onRefresh() {
    this.refreshList(this.data.curTab);
  },

  onOrderCardTap(e) {
    const { order } = e.currentTarget.dataset;
    wx.navigateTo({
      url: `/pages/order/order-detail/index?orderNo=${order.orderNo}`,
    });
  },
});
