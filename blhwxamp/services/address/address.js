

export const genAddressList = () => {
  return new Promise((resolve) => {
    const token = wx.getStorageSync('token');
    if (!token || token === '') {
      resolve([]);
    }
    wx.request({
      method: 'POST',
      url: 'https://wxamp.blhlm.com/rest/1.0/user/v1/address/list',
      data: {token},
      success: (res) => {
        // console.log(res.data)
        if (res.data.code === 0) {
          resolve(res.data.data);
        } else {
          wx.setStorageSync('token', '');
          resolve([]);
        }
      }
    })
  })
}


export const genAddress = (id) => {

  return new Promise((resolve) => {
    wx.request({
      method: 'POST',
      url: 'https://wxamp.blhlm.com/rest/1.0/user/v1/address/detail',
      data: {id},
      success: (res) => {
        // console.log(res.data)
        if (res.data.code === 0) {
          resolve(res.data.data);
        } else {
          wx.setStorageSync('token', '');
          resolve([]);
        }
      }
    })
  })

}