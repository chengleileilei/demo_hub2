// 简单的 store 模式
let store = {
    debug: true,
    state: window.sessionStorage.getItem('sharedState') ?
        JSON.parse(window.sessionStorage.getItem('sharedState')) : {
            message: {}
        },
    setMessageAction(newValue) {
        if (this.debug) console.log('setMessageAction triggered with', newValue)
        this.state.message = newValue;
    },
    clearMessageAction() {
        if (this.debug) console.log('clearMessageAction triggered')
        this.state.message = '';
    }
}
export default store

//     `需要注意，所有 store 中 state 的变更，都放置在 store 自身的 action 中去管理。
// 这种集中式状态管理能够被更容易地理解哪种类型的变更将会发生，以及它们是如何被触发。
// 当错误出现时，我们现在也会有一个 log 记录 bug 之前发生了什么`