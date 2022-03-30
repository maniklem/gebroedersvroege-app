<template>
  <div>
      <v-menu
        v-model="menu"
        :close-on-content-click="false"
        :nudge-top="270"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="field.date"
            :label="field.label"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
          <v-date-picker
          v-model="field.date"
          @input="menu = false"
          ></v-date-picker>
      </v-menu>
  </div>
</template>

<script>
  export default {
    props: ['fields'],
    data() {
        return {
          field: this.fields,
          menu: false,
          modal: false
        }
      },    
      created() {
          this.$emit("fields", this.field);
      }
  }
</script>

<style scoped>
</style>