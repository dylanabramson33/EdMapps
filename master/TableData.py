

class TableData(object):
	"""TableData takes a dictionary of POST datastructured in the following way:
		{'METADATA:ROWNUMBERCOLUMNUMBER'}.
		i.e. {'EnrichmentActivity01'}

		The purpose of this class is to assist in the dynamic creation of new Metadata table
		objects in the table view.

	"""


	def __init__(self,newModelData):
		initialSplitData = newModelData.split(':')
		self.metadata = initialSplitData[0]
		newSplitModelData = initialSplitData[1].split('#')
		self.row = int(newSplitModelData[0])
		self.column = int(newSplitModelData[1])



	def getColumnRangeForMetadata(list):
		"""
			args is a list of TableData objects


			Example of getColumnRangeForMetadata:
			getColumnRangeForMetadata('A|00,A|01,A|02,B|03')
			returns {"A" : [0,2], B : [3,3]}

			where in A|00 A is metadata and 00 is rowAndColumn

		"""
		tableDataColumnDictionary = {}
		tableDataList = list
		for tableData in tableDataList:
			metadata = getattr(tableData,"metadata")
			column = getattr(tableData,"column")
			try:
				tableDataColumnDictionary[metadata].append(column)
			except:
				tableDataColumnDictionary[metadata] = []
				tableDataColumnDictionary[metadata].append(column)

		tableDataRanges = {}
		#Reduces to the min and max value for each key in tableDataColumnDictionary
		for tableData in tableDataList:
			metadata = getattr(tableData,"metadata")
			tableDataRanges[tableData.metadata] = [min(tableDataColumnDictionary[metadata]),
																max(tableDataColumnDictionary[metadata])]


		return tableDataRanges
