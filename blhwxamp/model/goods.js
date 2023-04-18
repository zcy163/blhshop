import { genGood } from './good';

export function getGoodsList(page = 1, limit = 10, options = {}) {
  const host = 'https://wxamp.blhlm.com/rest/goods/v1/index'
  const url = `${host}?page=${page}&limit=${limit}`
  const data = {
    sort: options.sort || '',
    sequence: "-",
    filters: options.filters || '',
    search: options.search || ''
  }
  return new Promise((resolve, reject) => {
    // wx.showLoading({
    //   mask: true
    // })
    wx.request({
      method: 'POST',
      url,
      data,
      header: {},
      success (res) {
        if (res.data.data) {
          resolve(res.data.data.list || [])
        }
        resolve([])
      },
      fail (err) {
        reject(err)
      },
      complete: function() {
        // wx.hideLoading()
      }
    })
  })
  // return new Array(length).fill(0).map((_, idx) => genGood(idx + baseID));
}

export const goodsList = getGoodsList();
