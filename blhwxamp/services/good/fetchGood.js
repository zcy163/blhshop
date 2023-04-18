import { config } from '../../config/index';

/** 获取商品列表 */
function mockFetchGood(ID = 0, available = 1) {
  const { delay } = require('../_utils/delay');
  const { genGood } = require('../../model/good');
  // return delay().then(() => genGood(ID));
  return genGood(ID).then((item) => {
    // console.log(item)
    return {
      // ...item,
      spuId: `${ID}`,
      title: item.itemTitle,
      rate: item.commissionRate,
      zhuang: Number(item.itemPrice*(item.commissionRate/10)/10000).toFixed(2),
      desc: item.itemDescUrls || [],
      available: available,
      images: item?.itemGalleryUrls || [],
      maxLinePrice: item?.itemPrice,
      minSalePrice: item?.zkFinalPrice,
      skuList: item.skuList || [],
      soldNum: item.soldCountThirtyDays,
      isPutOnSale: 1,
      spuStockQuantity: 1
    };
  })
}

/** 获取商品列表 */
export function fetchGood(ID = 0) {
  if (config.useMock) {
    return mockFetchGood(ID);
  }
  return new Promise((resolve) => {
    resolve('real api');
  });
}
