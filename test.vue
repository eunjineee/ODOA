<input type="text" :value="search" class="search-input"  @input="searchUpdate($event.target.value)" @focus="focusSearch(true)" @blur="focusSearch(false)">
<b-list-group v-show="isFocusSearch" style="position:absolute; top:32px; left: 24px; z-index: 9;">
  <b-list-group-item class="flex-column align-items-start" v-for="searchResult in searchResults" :key="searchResult.id">
    <div @mousedown="goDetail(searchResult.id)" class="d-flex justify-content-between">
      <h5 class="mb-1">{{ searchResult.title }}</h5>
    </div>
  </b-list-group-item>
</b-list-group>