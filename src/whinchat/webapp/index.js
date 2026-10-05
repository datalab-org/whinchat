// Plugin manifest, collected into the webapp by `invoke dev.install`.
export default {
  apiVersion: 1,
  blocks: {
    chat: () => import("./ChatBlock.vue"),
  },
};
