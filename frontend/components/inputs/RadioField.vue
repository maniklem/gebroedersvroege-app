<template>
  <div>
    <v-radio-group v-model="field.selected" row>
        <v-radio
            v-for="(answer, idx) in field.answers"
            :key="idx"
            :label="answer"
            :value="answer"
        ></v-radio>
    </v-radio-group>
  </div>
</template>

<script>
  export default {
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