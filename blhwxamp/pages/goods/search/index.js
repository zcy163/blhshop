import {
  getSearchHistory,
  getSearchPopular,
} from '../../../services/good/fetchSearchHistory';
import Toast from 'tdesign-miniprogram/toast/index';

Page({
  data: {
    historyWords: [],
    popularWords: [],
    searchValue: '',
    dialog: {
      title: '确认删除当前历史记录',
      showCancelButton: true,
      message: '',
    },
    dialogShow: false,
  },

  deleteType: 0,
  deleteIndex: '',

  onShow() {
    this.queryHistory();
    this.queryPopular();
  },

  async queryHistory() {
    try {
      const data = await getSearchHistory();
      const code = 'Success';
      if (String(code).toUpperCase() === 'SUCCESS') {
        const { historyWords = [] } = data;
        this.setData({
          historyWords,
        });
      }
    } catch (error) {
      // console.error(error);
      Toast({
        context: this,
        message: error,
      });
    }
  },

  async queryPopular() {
    try {
      const data = await getSearchPopular();
      const code = 'Success';
      if (String(code).toUpperCase() === 'SUCCESS') {
        const { popularWords = [] } = data;
        this.setData({
          popularWords,
        });
      }
    } catch (error) {
      console.error(error);
    }
  },

  setSearchHistory(searchValue) {
    const search = wx.getStorageSync('search');
    if (search) {
      if (search.indexOf(searchValue) === -1) {
        search.unshift(searchValue)
        wx.setStorageSync('search', search)
        this.setData({
          historyWords: search
        })
      }
    } else {
      wx.setStorageSync('search', [searchValue])
      this.setData({
        historyWords: [searchValue]
      })
    }
  },

  confirm() {
    const { historyWords } = this.data;
    const { deleteType, deleteIndex } = this;
    historyWords.splice(deleteIndex, 1);
    if (deleteType === 0) {
      this.setData({
        historyWords,
        dialogShow: false,
      });
    } else {
      this.setData({ historyWords: [], dialogShow: false });
      wx.setStorageSync('search', [])
    }
  },

  close() {
    this.setData({ dialogShow: false });
  },

  handleClearHistory() {
    const { dialog } = this.data;
    this.deleteType = 1;
    this.setData({
      dialog: {
        ...dialog,
        message: '确认删除所有历史记录',
      },
      dialogShow: true,
    });
  },

  deleteCurr(e) {
    const { index } = e.currentTarget.dataset;
    const { dialog } = this.data;
    this.deleteIndex = index;
    this.setData({
      dialog: {
        ...dialog,
        message: '确认删除当前历史记录',
        deleteType: 0,
      },
      dialogShow: true,
    });
  },

  handleHistoryTap(e) {
    const { historyWords } = this.data;
    const { dataset } = e.currentTarget;
    const _searchValue = historyWords[dataset.index || 0] || '';
    if (_searchValue) {
      wx.setStorageSync('searchValue', _searchValue)
      wx.reLaunch({
        url: `/pages/home/home?searchValue=${_searchValue}`,
      });
    }
  },

  handleSubmit(e) {
    const value = e.detail.value;
    if (value && value.length === 0) return;
    this.setSearchHistory(value)
    wx.setStorageSync('searchValue', value)
    wx.reLaunch({
      url: `/pages/home/home?searchValue=${value}`,
    });
  },
});
