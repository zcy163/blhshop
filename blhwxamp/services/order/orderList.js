import { config } from '../../config/index';

/** 获取订单列表mock数据 */
function mockFetchOrders(params) {
  // const { delay } = require('../_utils/delay');
  // const { genOrders } = require('../../model/order/orderList');

  // return delay(200).then(() => genOrders(params));
  const host = 'https://wxamp.blhlm.com/rest/1.0/user/v1/order/list'
  const url = `${host}?limit=${params.parameter.pageSize}&page=${params.parameter.pageNum}`
  return new Promise((resolve, reject) => {
    wx.showLoading({
      mask: true
    })
    wx.request({
      method: 'POST',
      url,
      params: params,
      data: {
        token: wx.getStorageSync('token')
      },
      header: {},
      success (res) {
        // console.log(res.data)
        resolve(res.data.data)
      },
      fail (err) {
        reject(err)
      },
      complete: function() {
        wx.hideLoading()
      }
    })
  })
}

/** 获取订单列表数据 */
export function fetchOrders(params) {
  if (config.useMock) {
    return mockFetchOrders(params);
  }

  return new Promise((resolve) => {
    resolve('real api');
  });
}

/** 获取订单列表mock数据 */
function mockFetchOrdersCount(params) {
  const { delay } = require('../_utils/delay');
  const { genOrdersCount } = require('../../model/order/orderList');

  return delay().then(() => genOrdersCount(params));
}

/** 获取订单列表统计 */
export function fetchOrdersCount(params) {
  if (config.useMock) {
    return mockFetchOrdersCount(params);
  }

  return new Promise((resolve) => {
    resolve('real api');
  });
}
