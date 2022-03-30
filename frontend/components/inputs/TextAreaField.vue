<template>

          <v-textarea
            v-model="field.text"
            :label="field.label"
            outlined
          ></v-textarea>

</template>

<script>
export default {
    name: 'TextAreaField',
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