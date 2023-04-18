import { config } from '../../config/index';

/** 获取商品列表 */
function mockFetchGoodsList(pageIndex = 1, pageSize = 20, options) {
  // const { delay } = require('../_utils/delay');
  const { getGoodsList } = require('../../model/goods');
  // return delay().then(() =>
  //   getGoodsList(pageIndex, pageSize).map((item) => {
  //     return {
  //       spuId: item.spuId,
  //       thumb: item.primaryImage,
  //       title: item.title,
  //       price: item.minSalePrice,
  //       originPrice: item.maxLinePrice,
  //       tags: item.spuTagList.map((tag) => tag.title),
  //     };
  //   }),
  // );
  return getGoodsList(pageIndex, pageSize, options).then((goodsList) => {
    // console.log(goodsList)
    return goodsList.map((item) => {
      const itemCategoryName = item.item_category_name
        .split('>')
        .map((tag) => tag.split('/')[0]);

      return {
        spuId: item.item_id,
        thumb: item.item_img_url,
        title: item.item_title,
        price: item.item_price,
        volume: item.item_volume,
        stock: item.item_stock,
        type: item.web_url_type,
        rate: item.item_commission_rate,
        tags: [...new Set(itemCategoryName)].slice(0, 2),
      };
    });
  });
}

/** 获取商品列表 */
export function fetchGoodsList(pageIndex = 1, pageSize = 20, options) {
  if (config.useMock) {
    return mockFetchGoodsList(pageIndex, pageSize, options);
  }
  return new Promise((resolve) => {
    resolve('real api');
  });
}
