
import { fetchDeliveryAddressList } from '../../services/address/fetchAddress';

Component({
  properties: {
    addressVisible: {
      type: Boolean,
      value: false,
      observer(addressVisible) {
        if (addressVisible) {
          fetchDeliveryAddressList().then((res) => {
            const addresses = res.map((v) => {
              return { label: v.address, value: v.id }
            })
            this.setData({
              addresses,
              addressVisible,
            })
          })
        }
      },
    },
  },
  data: {
    addressVisible: false,
    addressText: '',
    addressValue: '',
    addresses: [],
  },

  ready() {
    
  },

  methods: {

    onPickerChange(e) {
      const { key } = e.currentTarget.dataset;
      const { value } = e.detail;
      const addressId = e.detail.value[0];
      // console.log(addressId);
      this.setData({
        [`${key}Visible`]: false,
        [`${key}Value`]: value,
        [`${key}Text`]: value.join(' '),
      });
      this.triggerEvent('select-address', {addressId});
    },
    
  },

});