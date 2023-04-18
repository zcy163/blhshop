import { config, cdnBase } from '../../config/index';

/** 获取首页数据 */
async function mockFetchHome() {
  const { delay } = require('../_utils/delay');
  const { genSwiperImageList } = require('../../model/swiper');
  const tabList = await getTabList();
  return delay().then(() => {
    const tabListMap = tabList.length ? tabList.map((tab) => {
      return {
        text: tab.category_name,
        key: tab.category_name,
      };
    }) : [];
    return {
      swiper: genSwiperImageList(),
      tabList: [
        {
          text: '精选推荐',
          key: '',
        },
        ...tabListMap,
      ],
      activityImg: `${cdnBase}/activity/banner.png`,
    };
  });
}

// 获取类目列表
function getTabList() {
  const host = 'https://wxamp.blhlm.com/rest/goods/v1/category';
  const url = `${host}`;
  const data = {};
  return new Promise((resolve, reject) => {
    wx.showLoading({
      mask: true,
    });
    wx.request({
      method: 'POST',
      url,
      data,
      header: {},
      success(res) {
        // console.log(res.data.data)
        resolve(res.data.data || []);
      },
      fail(err) {
        reject(err);
      },
      complete: function () {
        wx.hideLoading();
      },
    });
  });
}

/** 获取首页数据 */
export function fetchHome() {
  if (config.useMock) {
    return mockFetchHome();
  }
  return new Promise((resolve) => {
    resolve('real api');
  });
}
