/**
 pageState schemas

 Users page:
 {
   users: [] // list of objects generated by actions._userState
 }

 Data export page:
 {}

 Content import/export page:
 {
   taskList: [] // list of objects
   channelList: [] // list of objects
   wizardState: {} // object
 }

 **/

const initialState = {
  pageName: '',
  pageState: {
    channelList: [],
    wizardState: {},
    classes: [],
    users: [],
    taskList: [],
    modalShown: false,
    error: '',
    isBusy: false,
  },
};

export default initialState;