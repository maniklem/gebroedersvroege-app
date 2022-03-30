<template>
    <div>
        <v-col
          sm="12"
          md="12"
          lg="12"
        >
        <v-select
          v-model="field.selected"
          :items="field.answers"
          :label="field.label"
          outlined
          :value="field.selected"
        ></v-select>
      </v-col>
    </div>
</template>
<script>
    // :multiple="fields.multiple" You can make it multi select by just passing in multiple (true)
    export default {
        name: 'drop',
        props: ['fields'],
        data() {
          return {
            field: this.fields
          }
        },    
        created() {
            this.$emit("fields", this.field);
        },
    }
</script>

<style scoped>
</style>