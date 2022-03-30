<template>
          <v-text-field
            v-model="field.text"
            :label="field.label"
            outlined
          ></v-text-field>
</template>

<script>
export default {
    name: 'TextField',
    props:  ['fields'],
    data() {
        return {
            field: this.fields
        };
    },
    created() {
        this.$emit("fields", this.field);
    },
}
</script>

<style scoped>
</style>