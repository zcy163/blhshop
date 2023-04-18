
export const genSimpleUserInfo = () => {
  return new Promise((resolve) => {
    const token = wx.getStorageSync('token');
    if (!token || token === '') {
      resolve({});
    }
    wx.request({
      method: 'POST',
      url: 'https://wxamp.blhlm.com/rest/1.0/user/v1/token',
      data: {token},
      success: (res) => {
        // console.log(res.data)
        if (res.data.code === 0) {
          const userInfo = res.data.data;
          resolve(userInfo);
        } else {
          wx.setStorageSync('token', '');
          resolve({});
        }
      }
    })
  })
}