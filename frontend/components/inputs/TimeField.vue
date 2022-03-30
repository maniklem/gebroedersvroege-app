<template>
  <div>

        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :nudge-top="150"
          :return-value.sync="fields.time"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="fields.time"
              :label="fields.label"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="menu"
            v-model="fields.time"
            full-width
            @click:minute="$refs.menu.save(fields.time)"
          ></v-time-picker>
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