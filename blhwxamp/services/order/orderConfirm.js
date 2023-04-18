import { config } from '../../config/index';
import { mockIp, mockReqId } from '../../utils/mock';

/** 获取结算mock数据 */
function mockFetchSettleDetail(params) {
  const { delay } = require('../_utils/delay');
  const { genSettleDetail } = require('../../model/order/orderConfirm');

  return delay().then(() => genSettleDetail(params));
}

/** 提交mock订单 */
function mockDispatchCommitPay(params) {
  // const { delay } = require('../_utils/delay');

  // return delay().then(() => ({
  //   data: {
  //     isSuccess: true,
  //     tradeNo: '350930961469409099',
  //     payInfo: '{}',
  //     code: null,
  //     transactionId: 'E-200915180100299000',
  //     msg: null,
  //     interactId: '15145',
  //     channel: 'wechat',
  //     limitGoodsList: null,
  //   },
  //   code: 'Success',
  //   msg: null,
  //   requestId: mockReqId(),
  //   clientIp: mockIp(),
  //   rt: 891,
  //   success: true,
  // }));
  // console.log(params)

  const host = 'https://wxamp.blhlm.com/rest/1.0/user/v1/order/add'
  return new Promise((resolve, reject) => {
    wx.showLoading({
      mask: true
    })
    wx.request({
      method: 'POST',
      url: host,
      data: params,
      header: {},
      success (res) {
        // console.log(res.data)
        resolve(res.data)
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

/** 获取结算数据 */
export function fetchSettleDetail(params) {
  if (config.useMock) {
    return mockFetchSettleDetail(params);
  }

  return new Promise((resolve) => {
    resolve('real api');
  });
}

/* 提交订单 */
export function dispatchCommitPay(params) {
  if (config.useMock) {
    return mockDispatchCommitPay(params);
  }

  return new Promise((resolve) => {
    resolve('real api');
  });
}

/** 开发票 */
export function dispatchSupplementInvoice() {
  if (config.useMock) {
    const { delay } = require('../_utils/delay');
    return delay();
  }

  return new Promise((resolve) => {
    resolve('real api');
  });
}
